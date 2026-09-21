import json
import time
from pathlib import Path
from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY, MODELOS
from src.renderer import render_slide

class Gerador:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY não configurada")
        self.client = genai.Client(api_key=GEMINI_API_KEY)

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
                        temperature=0.45,
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

    def carrossel(self, pauta, outdir: Path):
        prompt = f"""
Crie um carrossel editorial em português para Uassi Mogone.

PAUTA:
Título-base: {pauta['titulo']}
Tema: {pauta['tema']}
Fonte: {pauta.get('fonte','')}

DIREÇÃO EDITORIAL:
- linguagem visual de referência: editorial premium, mais próxima de Forbes na capa e ritmo/tese inspirado em Tio Huli nos slides internos;
- nunca copiar marca, logotipo, layout proprietário ou redação de terceiros;
- exatamente 5 slides;
- slide 1 = capa editorial forte, headline curta, imagem real e alto contraste;
- slide 2 = contexto objetivo;
- slide 3 = tese central, mais seca e memorável;
- slide 4 = segundo momento visual forte, imagem + frase curta ou contraste;
- slide 5 = fechamento de tese, sem CTA genérico;
- uma ideia central por slide;
- menos texto e mais força de headline;
- linguagem direta, madura, não coach;
- nada de "5 coisas", "ninguém te conta", "você precisa saber";
- não inventar fatos;
- se a fonte não trouxer número no contexto, não invente número;
- textos realmente enxutos: evite parágrafos longos; priorize frases e blocos curtos;
- tom analítico e acessível;
- não atribua opinião pessoal nova a Uassi.

Retorne JSON:
{{
  "caption": "...",
  "slides": [
    {{"titulo":"...","corpo":"..."}},
    {{"titulo":"...","corpo":"..."}},
    {{"titulo":"...","corpo":"..."}},
    {{"titulo":"...","corpo":"..."}},
    {{"titulo":"...","corpo":"..."}}
  ]
}}
"""
        data = self._gerar_json(prompt)
        slides = data.get("slides", [])
        if len(slides) != 5:
            raise ValueError(f"Esperados 5 slides, recebidos {len(slides)}")

        imagens = []
        for i, s in enumerate(slides, start=1):
            path = outdir / f"slide_{i:02d}.png"
            render_slide(path, i, s.get("titulo",""), s.get("corpo",""), visual=i in (1,4))
            imagens.append(path)

        caption = data.get("caption","").strip()
        if pauta.get("fonte"):
            caption += f"\n\nFonte: {pauta['fonte']}"
        (outdir/"caption.txt").write_text(caption + "\n", encoding="utf-8")

        manifest = {
            "id": pauta["id"],
            "formato": "CARROSSEL",
            "caption": caption,
            "assets": [p.name for p in imagens],
            "source_url": pauta.get("fonte",""),
            "visual_style": "EDITORIAL_PREMIUM_FORBES_TIOHULI",
            "status": "READY_TO_PUBLISH",
        }
        (outdir/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
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
        roteiro = data.get("roteiro","").strip()
        legenda = data.get("legenda","").strip()
        (outdir/"roteiro.txt").write_text(roteiro+"\n", encoding="utf-8")
        (outdir/"caption.txt").write_text(legenda+"\n", encoding="utf-8")
        manifest = {
            "id": pauta["id"],
            "formato": "VIDEO_CURTO",
            "titulo": data.get("titulo", pauta["titulo"]),
            "gancho": data.get("gancho",""),
            "roteiro": roteiro,
            "caption": legenda,
            "source_url": pauta.get("fonte",""),
            "status": "READY_FOR_MANUAL_RECORDING",
        }
        (outdir/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        return manifest
