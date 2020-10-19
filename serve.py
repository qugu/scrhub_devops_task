import http.server as h
import requests


class proxy(h.BaseHTTPRequestHandler):
    def do_GET(self):
        # Preparing the request, make sure to include the client own headers.
        request = call_upstream(self.path, self.headers)
        # Return the user what we got from the downstream:
        for k, v in request.headers.items():
            self.send_header(k, v)
        self.send_response(request.status_code)
        self.end_headers()
        self.wfile.write(request.content)
        self.wfile.flush()
        self.close_connection


def call_upstream(url_path, headers):
    url = 'https://httpbin.org/{}'.format(url_path[1:])
    r = requests.get(url, headers=headers)
    return(r)


def run(server_class=h.HTTPServer, handler_class=h.BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, proxy)
    print('Starting server, use <Ctrl-C> to stop')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
