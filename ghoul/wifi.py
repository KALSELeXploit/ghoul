import os
def wifi(targ):
    print("\n[!] \033[92mScanning With Nmap..... \033[97m")
    os.system("nmap -T4 -A -v -Pn "+targ+"\24")

def wifiEx(targ,port):
    os.system("nc "+targ+port)
