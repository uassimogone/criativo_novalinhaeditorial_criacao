import json
import mimetypes
import requests
from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def _check():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise RuntimeError("Telegram não configurado")

def enviar_texto(texto):
    _check()
    r = requests.post(
        f"{BASE}/sendMessage",
        data={"chat_id": TELEGRAM_CHAT_ID, "text": texto},
        timeout=30,
    )
    r.raise_for_status()

def enviar_carrossel(titulo, imagens):
    _check()
    media = []
    files = {}
    for i, path in enumerate(imagens):
        key = f"f{i}"
        item = {"type": "photo", "media": f"attach://{key}"}
        if i == 0:
            item["caption"] = titulo[:900]
        media.append(item)
        files[key] = (path.name, open(path, "rb"), mimetypes.guess_type(path.name)[0] or "image/png")
    try:
        r = requests.post(
            f"{BASE}/sendMediaGroup",
            data={"chat_id": TELEGRAM_CHAT_ID, "media": json.dumps(media)},
            files=files,
            timeout=90,
        )
        r.raise_for_status()
    finally:
        for _, fh, _ in files.values():
            fh.close()
