#!/usr/bin/python3

import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python ftp_interaction.py <IP> <PORT>")
        sys.exit(1)

    IP = sys.argv[1]
    PORT = int(sys.argv[2])

    print("[+] Interagindo com o servidor FTP")
    
    try:
        # Criar socket e conectar
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(5)  # Define timeout de 5 segundos
        conn.connect((IP, PORT))
        
        # Receber banner inicial
        banner = conn.recv(1024).decode('utf-8', errors='ignore')
        print("[*] Banner recebido:")
        print(banner)

        # Enviar comando USER
        print("[+] Enviando comando USER")
        conn.send(str.encode("USER anonymous\r\n"))
        response = conn.recv(1024).decode('utf-8', errors='ignore')
        print("[*] Resposta:")
        print(response)

        # Enviar comando PASS
        print("[+] Enviando comando PASS")
        conn.send(str.encode("PASS anonymous\r\n"))
        response = conn.recv(1024).decode('utf-8', errors='ignore')
        print("[*] Resposta:")
        print(response)

    except socket.error as e:
        print(f"[!] Erro ao conectar ou enviar dados: {e}")
    finally:
        print("[+] Encerrando conexão")
        conn.close()


if __name__ == "__main__":
    main()
