from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        # 
        body = b'Hello World, do GET'
        #
        self.wfile.write(body)

    def do_POST(self):

        self._set_headers()

        body = b'Hello World, do POST'
        self.wfile.write(body)


if __name__ == '__main__': 
    host = ''
    port = 8000
    httpd = HTTPServer((host, port), MyHandler)
    print('serving at port', port)
    httpd.serve_forever()



