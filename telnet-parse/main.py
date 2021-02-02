import sys

def help():
	print ('Usage: python3 '+sys.argv[0]+' wireshark-packets.txt')
	sys.exit(0)

def main(input):
	file=open(input,"r")
	stream=file.read().split("\n\n")
	file.close()
	out=""
	for packet in stream:
		if "Destination Port: 23" in packet:
			packet=packet.split("Data: ")[-1]
			if packet=="\\r" or packet=="":
				print (out)
				out=""
			elif len(packet)==1:
				out+=packet

if __name__=="__main__":
	if len(sys.argv)<2:
		help()
	else:
		main(sys.argv[1])
