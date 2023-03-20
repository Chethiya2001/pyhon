from scapy.all import Ether, ARP, srp, conf
import sys
import time

def arp_scan(iface, ip_range):
    print("[+] Scanning",ip_range)
    curnt_time = time.time()
    print("[+] Scan started at ", time.ctime(curnt_time))
    conf.verb = 0
    brodcast = "ff:ff:ff:ff:ff:ff"
    ethr_layer = Ether(dst=brodcast) 
    arp_layer = ARP(pdst= ip_range)

    packet = ethr_layer/arp_layer

    ans, unans = srp(packet, iface= iface, timeout=2, inter=0.1)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print(ip,mac)
    duration = time.time() - curnt_time
    print("[+] Scan time " ,duration)



# scanner.py eth0 IP range
if __name__ =="__main__":
    iface = sys.argv[1] #eth0
    ip_range = sys.argv[2]
    arp_scan(ip_range, iface)
