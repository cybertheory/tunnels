
from tunnels import expose
import uvicorn

class TunnelApp:
    def __init__(self, app, port=8000):
        self.app = app
        self.port = port
        self.tunnel = None

    def run(self, *args, **kwargs):
        public_url, self.tunnel = expose(port=self.port)
        print(f"Public URL: {public_url}")
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

    def stop(self):
        if self.tunnel:
            self.tunnel.stop()
