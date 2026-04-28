import http.server
import socketserver
import webbrowser

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Dashboard running at: http://localhost:{PORT}")
    print("Open this URL in your browser")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()