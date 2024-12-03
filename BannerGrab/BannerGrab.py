#!/usr/bin/python3
import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python bannergrab.py <IP> <PORT>")
        sys.exit(1)

    IP = sys.argv[1]
    PORT = int(sys.argv[2])

    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(5)  
        conn.connect((IP, PORT))
        banner = conn.recv(1024).decode('utf-8', errors='ignore') 
        print(f"Banner recebido:\n{banner}")
    except socket.error as e:
        print(f"Erro ao conectar: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
