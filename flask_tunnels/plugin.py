
from tunnels import expose

class TunnelApp:
    def __init__(self, app, port=5000):
        self.app = app
        self.port = port
        self.tunnel = None

    def run(self, *args, **kwargs):
        public_url, self.tunnel = expose(port=self.port)
        print(f"Public URL: {public_url}")
        self.app.run(port=self.port)

    def stop(self):
        if self.tunnel:
            self.tunnel.stop()
