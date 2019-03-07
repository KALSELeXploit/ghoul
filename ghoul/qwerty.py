import os,sys
class warn:
      p = "\033[97m"

def osDetect(ip):
    print("[\033[96m+\033[97m] \033[92mScanning Os Detection...."+warn.p)
    os.system("nmap -O -Pn "+ip)
def nmap(ip):
    print("\n[\033[96m!\033[97m] \033[92mScanning Port With Nmap...."+warn.p)
    os.system("nmap -Pn "+ip)
def range(ip):
    print("\n[\033[96m!\033[97m] \033[92mScanning Range Port With Nmap...."+warn.p)
    os.system("nmap -p 1-3000 "+ip+" -Pn")
def udp(ip):
    print("\n[\033[96m!\033[97m] \033[92mScanning Udp Ports With Nmap...."+warn.p)
    os.system("nmap -sU -p 123,161,162 "+ip+" -Pn")
def netcat(ip,port):
    os.system("nc "+ip+" "+port)
def SSP(ip):
    print("\n[\033[96m!\033[97m] \033[92mScanning Selected Port - Ignore Discovery..."+warn.p)
    os.system("nmap -Pn -F "+ip+" -Pn")
