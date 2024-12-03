import socket, sys

host = sys.argv[1]

print(f"Host:{host}", socket.gethostbyname(host)) 