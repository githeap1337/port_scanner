# coding: utf-8

import socket
 
def scan_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if client.connect_ex((ip, port)):
        pass
    else:
        print(f"Порт {port} открыт")

if __name__ == "__main__":
    target = input('Target: ')
    ip = socket.gethostbyname(target)
    for port in range(1025):
        scan_port(ip, port)