# copy and pasted from ChatGPT

import psutil
import socket

def get_process_name(pid):
    try:
        return psutil.Process(pid).name()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return "Unknown"

def scan_local_connections():
    connections = psutil.net_connections(kind="tcp")

    print(f"{'Local Address':<25} {'Port':<8} {'State':<12} {'PID':<8} Process")

    for conn in connections:
        if conn.laddr:
            ip, port = conn.laddr

            pid = conn.pid if conn.pid else 0
            process_name = get_process_name(pid) if pid else "System"

            print(f"{ip:<25} {port:<8} {conn.status:<12} {pid:<8} {process_name}")

if __name__ == "__main__":
    scan_local_connections()