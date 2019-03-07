import requests,json
def public():
             scan = "https://api.myip.com"
             sabyanEru=json.loads(requests.get(scan).text)
             print("[*] Your IP Public : "+str(sabyanEru["ip"]))
