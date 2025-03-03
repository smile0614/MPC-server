import os
import json
from datetime import datetime

def find_files(path_fragment):
    result = []
    for root, dirs, files in os.walk('/'):
        for file in files:
            if path_fragment in os.path.join(root, file):
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                result.append({
                    "name": file,
                    "path": file_path,
                    "size": file_stat.st_size,
                    "created": datetime.fromtimestamp(file_stat.st_ctime).isoformat()
                })
    return result

def handle_request(request):
    if request['method'] == 'find_files':
        return {'result': find_files(request['params']['path_fragment'])}
    else:
        return {'error': 'Unknown method'}

def main():
    import http.server
    import socketserver

    class MCPRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            request = json.loads(body)
            response = handle_request(request)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

    with socketserver.TCPServer(("", 8080), MCPRequestHandler) as httpd:
        print("MCP Server started on port 8080")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
