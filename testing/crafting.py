from scapy.all import *
import time
dst = "10.0.0.2"

# FIRST ROUND OF PACKETS
src = "ruby.cirt.vt.edu"
dport = 20
flags = "S"                           

icmp.type = type
icmp.chksum = checksum


packet = ip/icmp
#icmp = ICMP()
#icmp.type = type
#icmp.chksum = checksum
#packet = scapy.IP(src=src, dst=dst)/(scapy.ICMP(type=type, chksum=checksum))

send(packet, count=35)

time.sleep(3)

# THIRD ROUND OF PACKETS

src = "violet.cirt.vt.edu"
flags = "SFR"
data = "team10"

sport = 32700

for x in range(0, 10):
	ip = IP(src=src, dst=dst)
	tcp = TCP(sport=sport)
	payload = Raw(data)
	packet = (ip/tcp)/payload
	send(packet)
	sport = sport + 1