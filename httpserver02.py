from http.server import HTTPServer, SimpleHTTPRequestHandler



class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        body = b'Hello World, do GET'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        body = b'Hello World, do POST test'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__': 
    host = '127.0.0.1'
    port = 8000
    httpd = HTTPServer((host, port), MyHandler)
    print('serving at port', port)
    httpd.serve_forever()



