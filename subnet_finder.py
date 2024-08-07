# a script to tell you what subnets a ipv4 address belongs to
from scapy.all import ARP, Ether, srp
import ipaddress as ip
import sys

def finding_subnets(ip_address):
    try:
        ipv4_addr = ip.ip_address(ip_address)
        for subnet in subnets:
            if ipv4_addr in subnet:
                return subnet
            return "No matching subnet has been found"
    except ValueError:
            return "Invalid IPv4 address"

def arp_scan(subnet):
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)[0]
    
    up_host = []

    for sent, received in result:
        up_host.append({'ip': received.psrc, 'mac': received.hwsrc})
    return up_host

def main():
    if len(sys.argv) < 2:
        print("usage ; python3 subnet_finder.py 192.168.1.127")
        return
    IP = sys.argv[1]
    subnet = finding_subnets(IP)
    if subnet:
        print("Subnet found:", subnet)
        print("Scanning subnet {} for alive hosts".format(subnet))
        live_hosts = arp_scan(subnet)
        print("Live hosts found:")
        for host in live_hosts:
            print("IP:", host['ip'], "\tMAC:", host['mac'])
    else:
        print("Invalid IP address or not within private IP space.")
    

if __name__ == "__main__":
    subnets = [   
        ip.ip_network('10.0.0.0/8'),
        ip.ip_network('172.16.0.0/12'),
        ip.ip_network('192.168.0.0/16')
    ]
    main()