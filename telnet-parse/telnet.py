import sys
import os

def start_shell(input):
	shell = os.system('grep -A 44 23 ' + input + ' | grep Data: > .raw-telnet.txt')

def open_raw():
	global massive,sum
	input = open (".raw-telnet.txt","r")
	massive = input.read().split(" ")
	for i in massive:
		if i == "Data:":
			massive.remove(i)
	for i in massive:
		if i=="":
			massive.remove(i)

	input.close()
	sum = ""
	for i in massive:
		sum +=i

	massive = sum.split("\n")
	sum=""


def sort():
	for i in massive:
		if i== "\\r":
			massive.insert(massive.index(i),"\n")
			massive.remove(i)
		if i== "":
			massive.insert(massive.index(i), " ")
			massive.remove(i)

	x=1
	while x!=len(massive):
		if massive[x] == "\\177" and massive[x-1]=="\n":
			massive.pop(x)
			x=0

		elif massive[x] == "\\177":
			massive.pop(x)
			massive.pop(x-1)
			x=0
		x+=1

	x=1
	while x != len(massive):
		if len(massive[x]) > 1:
			massive.remove(massive[x])
			x=0
		x+=1
def result():
	global sum
	for i in massive:
		sum+=i
	print (sum)
	shell = os.system('rm .raw-telnet.txt')

if __name__ == '__main__':
	if len (sys.argv) == 2:
		start_shell(sys.argv[1])
		open_raw()
		sort()
		result()
	else:
		print ('Usage: python3 telnet.py wireshark-packets.txt')
