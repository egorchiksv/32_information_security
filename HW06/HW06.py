# Написать программу на Python, которая будет проводить сканирование с использованием nmap.
import nmap

nm = nmap.PortScanner()
IP = "192.168.1.113"
nm.scan(IP, arguments="-sO")

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))