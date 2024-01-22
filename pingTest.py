from ping3 import ping
import time

file = open("ip_list.txt", "r") #opens the file and reads it in
readFile = file.readlines() #reads each line and puts it into a list
ipList = [line.rstrip('\n') for line in readFile]

def pingTest():
    for eachIP in ipList:
#        print(eachIP)
        testPing = ping(eachIP)
#        print(testPing)
        boolPing = bool(testPing)
        if boolPing is True:
            print(eachIP + " is ONLINE.")
        else:
            print(eachIP + " is OFFLINE.")
            
while True:
    pingTest()
    time.sleep(30)#wait 30 seconds and then try again
