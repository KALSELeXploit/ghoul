#Apakah OOP dah Bener?
import os,sys 
from ghoul import qwerty as sabyan
from ghoul import ip as chitanda
from ghoul import wifi as chiichan
import time 
class warn:
      p = "\033[97m"
os.system("clear")
print("""   

  * |\___/|   *     *
 *  )     (      *    *    
   =\     /  *
     )===(        
 *  /     \       Coding By Pengabdi Sabyan
    |     |       Team : Kalsel[\033[96mE\033[97m]Xploit
   /       \\      Greetz : \033[91m407\033[97mAeX
   \       /
   _/\_/\_/\_

Cuman Tools Buat Latihan Uler Gan Bukan Apa2 h3h3""")

#.format(chitanda.public()))
print("\033[92mSystem Information : \033[97m")
os.system("uname -a")
print("""
[\033[92m1\033[97m].eploit cystim  Situs Open Port
[\033[92m2\033[97m].eploit Jaringan Wifi
[\033[92m3\033[97m].Mempercepat Jaringan Wifi
""")

home = input("[\033[92m?\033[97m] SabyanChan/>: ")

if home == "1":
               ip = input("\n[\033[96m?\033[97m] Enter IP Address Or Site Target : "+warn.p)
               sabyan.osDetect(ip)
               sabyan.nmap(ip)
               sabyan.range(ip)
               sabyan.udp(ip)
               sabyan.SSP(ip)
               print("\n[\033[96m!\033[97m] \033[92mExploit Network Server With Netcat...."+warn.p)
               port = input("[\033[96m?\033[97m] Enter Open Port : ")
               sabyan.netcat(ip,port)

elif home == "2":
                 print("\n[\033[93m!\033[97m] \033[92mScanning IP address...."+warn.p)
                 time.sleep(3)
                 os.system("route -n")
                 IP = input("\n[\033[92m?\033[97m] Enter IP Address : ")
                 chiichan.wifi(IP)
                 print("\n[!] \033[92mExploit With Netcat....  \033[97m")
                 PORT = input("[\033[92m?\033[97m] Enter Open Port : ")
                 chiichan.wifiEx(IP,PORT)
elif home == "3":
                 print("\n[\033[92m!\033[97m] \033[92mScanning IP Address...."+warn.p)
                 time.sleep(3)
                 os.system("route -n")
                 gbs = input("\n[!] Masukan IP Address Default : ")
                 print("[\033[95m!\033[97m] \033[92mNgeping Di IP %s ......"%gbs+warn.p)
                 os.system("ping -b "+gbs)
else:
     print("[\033[3m√] \033[92mO'Hayo Watashi Pilihan Kamu Ga Ada ^^"+warn.p)
     
