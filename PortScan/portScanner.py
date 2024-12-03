#!/usr/bin/python3
import socket
import sys

def main():
    if len(sys.argv) <= 1:
        print("----------------------------------------")
        print("[-] Uso: python3 portScanner.py <ip>")
        print("[-] Uso: python3 portScanner.py <ip> <range port>")
        print("----------------------------------------")
    else:

        IP = sys.argv[1]
        PORTLIST = []
        PORTRANGE = 65537
        if(len(sys.argv) == 3):
            PORTRANGE = int(sys.argv[2])+1

        print("-------------------------------------------------------------------------")
        print(f"[+] Iniciando scanner no host: {IP} Range de portas 1 - {PORTRANGE -1}")
        print("-------------------------------------------------------------------------")

        try:
            for port in range(1, PORTRANGE):
                socketer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socketer.settimeout(0.5) 
                res = socketer.connect_ex((IP, port))
                if res == 0:
                    PORTLIST.append(f"{IP}:{port}")
                socketer.close()
        except socket.error as e:
            print(f"Erro ao conectar: {e}")
        print("------------------------")
        for port in PORTLIST:
            print(f"[#] Host {port} ")
        print("------------------------")

if __name__ == "__main__":
    main()