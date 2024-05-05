# https_server.py

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

# Define the address and port
address = '0.0.0.0'
port = 8000

# Specify the directory to serve files from
directory = '.'

# Specify the SSL certificate and key file paths
certfile = 'server.crt'
keyfile = 'server.key'

# Create an HTTP server with SSL support
httpd = HTTPServer((address, port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)

print(f"Starting HTTPS server on {address}:{port}...")
httpd.serve_forever()
