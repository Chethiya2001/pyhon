from scapy.all import IP,ICMP, sr1 , ls

ip_layer = IP(src="192.168.1.3", dst="www.learn.esoft.lk")
icmp_req= ICMP()

# print(ip_layer.src)
# print(ip_layer.dst)

# print(ip_layer.summary())
print(ls(ip_layer))

# packet =  ip_layer / icmp_req #combine together

# recieved_pkt= sr1(packet)

# if recieved_pkt:
#     print(recieved_pkt.show())
