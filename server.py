#!/usr/bin/env python3
"""
Minimal HTTP server for hello world webpage
Usage: python server.py
Access: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop server")
        
        # Auto-open browser to hello world page
        webbrowser.open(f'http://localhost:{PORT}/hello_world.html')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

if __name__ == "__main__":
    main()
