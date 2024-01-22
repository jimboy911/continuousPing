from ping3 import ping

ipList = [
    '8.8.8.8', #google
    '1.1.1.1', #cloudflare
    '192.168.10.101' #this one should fail
    ]

def pingTest():
    for eachIP in ipList:
        testPing = ping(eachIP)
        boolPing = bool(testPing)
        if boolPing is True:
            print(eachIP + " is ONLINE.")
        else:
            print(eachIP + " is OFFLINE.")
            
while True:
    pingTest()