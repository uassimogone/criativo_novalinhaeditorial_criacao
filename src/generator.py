import json
import time
from pathlib import Path

from google import genai
from google.genai import types

from src.config import GEMINI_API_KEY, MODELOS
from src.image_researcher import ImageResearcher
from src.renderer import (
    render_slide,
    FAMILIES,
    FAMILY_DARK,
    FAMILY_MINIMAL,
    FAMILY_LIGHT,
    FAMILY_COMPARE,
    FAMILY_PHOTO,
    FAMILY_DATA,
)


class Gerador:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY não configurada")
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.images = ImageResearcher()

    def _gerar_json(self, prompt):
        erros = []
        for modelo in MODELOS:
            try:
                print(f"Tentando {modelo}")
                r = self.client.models.generate_content(
                    model=modelo,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        temperature=0.38,
                    ),
                )
                if not r.text:
                    raise ValueError("resposta vazia")
                return json.loads(r.text)
            except Exception as exc:
                erros.append(f"{modelo}: {exc}")
                print(erros[-1])
                time.sleep(2)
        raise RuntimeError("Falha em todos os modelos: " + " | ".join(erros))

    @staticmethod
    def _family_instruction(family):
        return {
            FAMILY_DARK: "Editorial Fotográfico Escuro: tensão, fotografia, contraste, clima de revista premium.",
            FAMILY_MINIMAL: "Minimalista Tipográfico: espaço negativo, frase-tese, quase nenhuma imagem.",
            FAMILY_LIGHT: "Editorial Claro/Revista: off-white, análise sóbria, estrutura de matéria contemporânea.",
            FAMILY_COMPARE: "Comparação Visual: contraste promessa x realidade ou duas ideias opostas.",
            FAMILY_PHOTO: "Fotografia Protagonista: imagem ocupa grande parte da peça e o texto é mínimo.",
            FAMILY_DATA: "Dado/Diagrama Editorial: relação ou dado em destaque, sem cara de dashboard corporativo.",
        }.get(family, "Editorial Claro/Revista.")

    def _carrossel_data(self, pauta, family):
        slides_aprovados = pauta.get("slides_aprovados")
        if slides_aprovados and len(slides_aprovados) == 5:
            prompt = f"""
Escreva apenas uma legenda para um carrossel editorial de Uassi Mogone.

PAUTA:
{pauta['titulo']}
Tema: {pauta['tema']}
Fonte: {pauta.get('fonte','')}

SLIDES JÁ APROVADOS E IMUTÁVEIS:
{json.dumps(slides_aprovados, ensure_ascii=False)}

REGRAS DA LEGENDA:
- português natural;
- direta, madura e analítica;
- sem tom de coach;
- não repetir todos os slides;
- contextualizar a tese em até 900 caracteres;
- não inventar fatos;
- não atribuir opinião pessoal nova;
- sem CTA genérico.

Retorne JSON:
{{"caption":"..."}}
"""
            data = self._gerar_json(prompt)
            return {"caption": data.get("caption", ""), "slides": slides_aprovados}

        prompt = f"""
Crie um carrossel editorial em português para Uassi Mogone.

PAUTA:
Título-base: {pauta['titulo']}
Tema: {pauta['tema']}
Fonte: {pauta.get('fonte','')}

FAMÍLIA VISUAL DEFINIDA:
{family}
{self._family_instruction(family)}

DIREÇÃO EDITORIAL:
- exatamente 5 slides;
- slide 1 = capa forte e curta;
- slide 2 = contexto objetivo;
- slide 3 = tese central seca e memorável;
- slide 4 = segundo momento visual forte;
- slide 5 = fechamento de tese, sem CTA genérico;
- uma ideia central por slide;
- pouco texto;
- linguagem direta, madura e acessível;
- nada de "5 coisas", "ninguém te conta", "você precisa saber";
- não inventar fatos ou números;
- não atribuir opinião pessoal nova a Uassi;
- evitar linguagem jurídica técnica desnecessária;
- pensar como uma matéria editorial premium, não como post de agência.

Para os slides 1 e 4, crie também uma consulta curta EM INGLÊS para encontrar fotografia real relacionada ao assunto no Wikimedia Commons.
Nos demais slides, visual_query pode ser vazio.

Retorne JSON:
{{
  "caption": "...",
  "slides": [
    {{"titulo":"...","corpo":"...","visual_query":"..."}},
    {{"titulo":"...","corpo":"...","visual_query":""}},
    {{"titulo":"...","corpo":"...","visual_query":""}},
    {{"titulo":"...","corpo":"...","visual_query":"..."}},
    {{"titulo":"...","corpo":"...","visual_query":""}}
  ]
}}
"""
        return self._gerar_json(prompt)

    def carrossel(self, pauta, outdir: Path):
        family = pauta.get("visual_family", FAMILY_LIGHT)
        if family not in FAMILIES:
            family = FAMILY_LIGHT

        data = self._carrossel_data(pauta, family)
        slides = data.get("slides", [])
        if len(slides) != 5:
            raise ValueError(f"Esperados 5 slides, recebidos {len(slides)}")

        imagens = []
        visual_sources = []
        assets_dir = outdir / "assets"

        forced_queries = pauta.get("visual_queries") or {}

        for i, s in enumerate(slides, start=1):
            path = outdir / f"slide_{i:02d}.png"
            visual_asset = None

            wants_photo = (
                family in {FAMILY_DARK, FAMILY_LIGHT, FAMILY_COMPARE, FAMILY_PHOTO}
                and i in (1, 4)
            )
            if family == FAMILY_PHOTO and i == 5:
                wants_photo = True

            if wants_photo:
                query = str(forced_queries.get(str(i), "") or s.get("visual_query", "")).strip()
                if query:
                    visual_asset = self.images.find_and_download(
                        query=query,
                        content_id=f"{pauta['id']}_s{i}",
                        target_dir=assets_dir,
                    )
                    if visual_asset:
                        visual_sources.append({
                            "slide": i,
                            "source_url": visual_asset.source_url,
                            "license": visual_asset.license_name,
                            "creator": visual_asset.creator,
                            "title": visual_asset.title,
                        })

            render_slide(
                path=path,
                numero=i,
                titulo=s.get("titulo", ""),
                corpo=s.get("corpo", ""),
                family=family,
                visual_path=visual_asset.local_path if visual_asset else None,
            )
            imagens.append(path)

        caption = data.get("caption", "").strip()
        if pauta.get("fonte"):
            caption += f"\n\nFonte: {pauta['fonte']}"

        credits = []
        for src in visual_sources:
            lic = (src.get("license") or "").casefold()
            if "cc by" in lic or "cc-by" in lic:
                creator = src.get("creator") or "autor indicado no Wikimedia Commons"
                credits.append(f"Imagem slide {src['slide']}: {creator} — {src['license']} — {src['source_url']}")
        if credits:
            caption += "\n\nCréditos de imagem:\n" + "\n".join(credits)

        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "caption.txt").write_text(caption + "\n", encoding="utf-8")

        manifest = {
            "id": pauta["id"],
            "formato": "CARROSSEL",
            "caption": caption,
            "assets": [p.name for p in imagens],
            "source_url": pauta.get("fonte", ""),
            "visual_family": family,
            "visual_sources": visual_sources,
            "visual_revision": pauta.get("visual_revision", 1),
            "status": "READY_TO_PUBLISH",
        }
        (outdir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return manifest, imagens

    def video(self, pauta, outdir: Path):
        prompt = f"""
Crie roteiro de vídeo curto para Uassi Mogone.

PAUTA:
Título-base: {pauta['titulo']}
Tema: {pauta['tema']}

REGRAS:
- 60 a 90 segundos;
- fala oral, direta e natural;
- ideia central clara;
- sem tom de coach;
- sem exagero ou clickbait;
- não atribuir experiência ou opinião pessoal nova sem base;
- fechamento reflexivo, não CTA genérico.

Retorne JSON:
{{"titulo":"...","gancho":"...","roteiro":"...","legenda":"..."}}
"""
        data = self._gerar_json(prompt)
        outdir.mkdir(parents=True, exist_ok=True)
        roteiro = data.get("roteiro", "").strip()
        legenda = data.get("legenda", "").strip()
        (outdir / "roteiro.txt").write_text(roteiro + "\n", encoding="utf-8")
        (outdir / "caption.txt").write_text(legenda + "\n", encoding="utf-8")
        manifest = {
            "id": pauta["id"],
            "formato": "VIDEO_CURTO",
            "titulo": data.get("titulo", pauta["titulo"]),
            "gancho": data.get("gancho", ""),
            "roteiro": roteiro,
            "caption": legenda,
            "source_url": pauta.get("fonte", ""),
            "status": "READY_FOR_MANUAL_RECORDING",
        }
        (outdir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return manifest
