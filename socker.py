#!/usr/bin/python3
import socket
import sys

def main():
    if len(sys.argv)  <= 2:
        print("----------------------------------------")
        print("[-] Uso: python3 scanner.py <ip> <port>")
        print("----------------------------------------")
    else:
        ip = "192.168.0.1"
        port = 82

        try:
            socketer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socketer.settimeout(2)  
            res = socketer.connect_ex((ip, port))

            if res == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Close")

            socketer.close()
        except socket.error as e:
            print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    main()