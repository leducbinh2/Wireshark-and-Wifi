import os
import subprocess
import time
import sys

# --- CẤU HÌNH ---
IFACE_AP = "wlan0"      # Card TP-Link V1
IFACE_WAN = "wlan1"     # Card Intel (Internet)
GATEWAY_IP = "10.0.0.1" 
CONF_PATH = "/home/kali/Desktop"

def run_cmd(cmd):
    subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def kill_conflicts():
    print("[!] Đang diệt các tiến trình gây xung đột DNS...")
    os.system("sudo systemctl stop systemd-resolved > /dev/null 2>&1")
    os.system("sudo systemctl disable systemd-resolved > /dev/null 2>&1")
    os.system("sudo killall dnsmasq hostapd wireshark wpa_supplicant > /dev/null 2>&1")

def setup_network():
    print("[+] Đang cấu hình Network & Firewall...")
    os.system("sudo iptables -F")
    os.system("sudo iptables -t nat -F")
    os.system(f"sudo ifconfig {IFACE_AP} up")
    os.system(f"sudo ifconfig {IFACE_AP} {GATEWAY_IP} netmask 255.255.255.0")
    os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null")
    os.system(f"sudo iptables -t nat -A POSTROUTING -o {IFACE_WAN} -j MASQUERADE")
    os.system(f"sudo iptables -A FORWARD -i {IFACE_AP} -o {IFACE_WAN} -j ACCEPT")
    os.system(f"sudo iptables -A FORWARD -i {IFACE_WAN} -o {IFACE_AP} -j ACCEPT")
    os.system(f"sudo iptables -A FORWARD -p udp --dport 53 -j ACCEPT")
    os.system(f"sudo iptables -A FORWARD -p tcp --dport 53 -j ACCEPT")

def start_services():
    print("[+] Đang khởi động Mang..")
    run_cmd(f"sudo dnsmasq -C {CONF_PATH}/dnsmasq.conf -d")
    run_cmd(f"sudo hostapd {CONF_PATH}/hostapd.conf")
    
    time.sleep(3)
    print("[+] Mở Wireshark...")
    run_cmd(f"sudo wireshark -k -i {IFACE_AP}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Khe roi !")
        sys.exit(1)
    try:
        kill_conflicts() 
        setup_network()
        start_services()
        print("\n[V] HỆ THỐNG ĐÃ CHẠY! Hãy kết nối.")
        print("chọn 'Tin cậy'.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[-] Đang dọn dẹp...")
        os.system("sudo killall dnsmasq hostapd")
        os.system("sudo systemctl start systemd-resolved")
