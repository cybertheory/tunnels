
from .binary import ensure_inlets_binary
import subprocess

class Tunnel:
    def __init__(self, port, server_url, token):
        self.port = port
        self.server_url = server_url
        self.token = token
        self.proc = None

    def start(self):
        binary = ensure_inlets_binary()
        cmd = [
            str(binary),
            "client",
            "--remote", self.server_url,
            "--upstream", f"http://localhost:{self.port}",
            "--token", self.token,
        ]
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stop(self):
        if self.proc:
            self.proc.terminate()
            self.proc.wait()

    def is_running(self):
        return self.proc and self.proc.poll() is None

def expose(port=5000, server="wss://tunnels.run", token="localdev"):
    tunnel = Tunnel(port, server, token)
    tunnel.start()
    public_url = f"https://{token}.tunnels.run"
    return public_url, tunnel
