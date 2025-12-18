import socket
import threading
import logging

logging.basicConfig(filename="scan.log", level=logging.INFO)

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print(f"[OPEN] Port {port}")
        logging.info(f"OPEN Port {port}")
        s.close()
    except:
        print(f"[CLOSED] Port {port}")
        logging.info(f"CLOSED Port {port}")

host = input("Target IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

threads = []

for port in range(start, end + 1):
    t = threading.Thread(target=scan_port, args=(host, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Scan completed")
