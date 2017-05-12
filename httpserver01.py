# -*- coding: utf-8 -*-
#!/usr/bin/env python

# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging



# HTTPRequestHandler class
class MyRequestHandler(BaseHTTPRequestHandler):
 
    # GET
    def do_GET(self):
        logging.info("get path : " + self.path);

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world, GET <br/>" + "get path : " + self.path
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    # POST
    def do_POST(self):
        body = b'Hello World, do POST'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

def run():
    print('starting server...')
    
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('running server...')
    httpd.serve_forever()
   
run()

