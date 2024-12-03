#!/usr/bin/python
import sys

if len(sys.argv) <= 2:
    print("----------------------------------------")
    print("[-] Uso: python3 scanner.py <ip> <port>")
    print("----------------------------------------")
else:
    print(f"[+] Varrendo IP: {sys.argv[1]}, na porta: {sys.argv[2]}")
