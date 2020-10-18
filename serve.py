import http.server as h
# from socketserver import TCPServer as tcp
from urllib import request

port = 9097


class MyProxy(h.BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        self.send_response(200)
        self.end_headers()
        print(self.path)
        # self.copyfile(request.urlopen(url), self.wfile)

def run(server_class=h.HTTPServer, handler_class=h.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, MyProxy)
    httpd.serve_forever()


run()