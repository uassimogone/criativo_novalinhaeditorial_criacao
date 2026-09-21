import json
from pathlib import Path

PATH = Path("data/historico_criativos.json")

def carregar():
    if not PATH.exists():
        return []
    return json.loads(PATH.read_text(encoding="utf-8") or "[]")

def salvar(itens):
    PATH.parent.mkdir(parents=True, exist_ok=True)
    PATH.write_text(json.dumps(itens, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
