
import os
import platform
import requests
from pathlib import Path

BIN_DIR = Path.home() / ".tunnels" / "bin"
INLETS_PATH = BIN_DIR / "inlets"

def ensure_inlets_binary():
    if INLETS_PATH.exists():
        return INLETS_PATH

    os_name = platform.system().lower()
    arch = "amd64"
    url = f"https://github.com/inlets/inlets/releases/latest/download/inlets_{os_name}_{arch}"

    BIN_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading inlets from {url}")
    binary = requests.get(url).content
    INLETS_PATH.write_bytes(binary)
    INLETS_PATH.chmod(0o755)
    return INLETS_PATH
