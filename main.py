import json
from datetime import datetime
from pathlib import Path
from src.generator import Gerador
from src.history import carregar, salvar
from src.telegram_bot import enviar_texto, enviar_carrossel

def main():
    pautas = json.loads(Path("data/pautas_aprovadas.json").read_text(encoding="utf-8"))
    historico = carregar()
    feitos = {x.get("id") for x in historico}

    pendentes = [p for p in pautas if p.get("status") == "APPROVED" and p.get("id") not in feitos]
    if not pendentes:
        enviar_texto("CRIADOR EDITORIAL — nenhuma pauta nova aprovada para gerar.")
        print("Nenhuma pauta pendente.")
        return

    gerador = Gerador()
    lote = datetime.now().strftime("%Y-%m-%d")
    novos = []

    for pauta in pendentes:
        outdir = Path("output") / lote / pauta["id"]
        if pauta["formato_final"] == "CARROSSEL":
            manifest, imagens = gerador.carrossel(pauta, outdir)
            enviar_carrossel(f"{pauta['id']} — CARROSSEL PRONTO", imagens)
            enviar_texto(f"Legenda:\n{manifest['caption'][:3500]}")
        elif pauta["formato_final"] == "VIDEO_CURTO":
            manifest = gerador.video(pauta, outdir)
            enviar_texto(
                f"{pauta['id']} — ROTEIRO DE VÍDEO\n\n"
                f"{manifest['gancho']}\n\n{manifest['roteiro']}\n\n"
                f"Legenda:\n{manifest['caption']}"
            )
        else:
            print(f"Formato ainda não implementado: {pauta['formato_final']}")
            continue

        novos.append({"id": pauta["id"], "formato": pauta["formato_final"], "lote": lote})

    salvar(historico + novos)
    print(f"{len(novos)} criativos gerados.")

if __name__ == "__main__":
    main()
