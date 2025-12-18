# TCP Port Scanner

A simple TCP port scanner built using Python as part of the SYNTECXHUB Cyber Security Internship.

## Description
This project scans a given range of TCP ports on a target host and identifies whether each port is open or closed using socket programming.  
Multithreading is used to improve scanning speed, and results are logged into a file.

## Features
- Scan a single host
- Scan a range of ports
- Detect open and closed ports
- Timeout handling
- Multithreading for faster execution
- Logging scan results to a file

## Technologies Used
- Python
- socket
- threading
- logging

## How to Run

1. Ensure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open terminal or command prompt inside the project folder.
4. Run the program using:

```bash
python tcp_port_scanner.py
5.Enter the required inputs:
   - Target IP address
   - Start port
   - End port

6.View the output in the terminal and in the `scan.log` file.
## Sample Output
   Target IP: 127.0.0.1
   Start port: 75
   End port: 85

   [CLOSED] Port 75
   [CLOSED] Port 76
   [OPEN] Port 80

Scan completed
## Disclaimer
This project is created for educational purposes only.  
Scan only systems you own or have explicit permission to test.
