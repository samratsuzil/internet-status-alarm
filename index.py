# from playsound import playsound
# from time import sleep
# import csv
# from datetime import datetime

# import speedtest   
# from gtts import gTTS 
# import os
# import pyspeedtest


# text="Your Internet is Working"

# st=pyspeedtest.SpeedTest()
# speedtest_result.ping()
# st.download()

# speech=gTTS(text,slow=False)
# speech.save('sample.mp3')
# # os.system('sample.mp3')
# playsound('sample.mp3')

# speedtest_result=speedtest.Speedtest()


# download=speedtest_result.download()
# speech=gTTS(download,slow=False)
# speech.save('speed.mp3')
# playsound('speed.mp3')

# print("Enter Interval of Monitoring (in seconds):")
# monitoring_interval=int(input())

from playsound import playsound
from time import sleep
import csv
from datetime import datetime

f=open('logs.csv','w')
writer = csv.writer(f)

monitoring_interval=10

def ping(host):
    import subprocess, platform
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True
    return subprocess.call(args, shell=need_sh) == 0

prev_status=ping("google.com")
writer.writerow(["Time","Internet Status"])
if prev_status:
    playsound('success.mp3')
    writer.writerow([datetime.now(),"Up"])
else:
    playsound('failure.mp3')
    writer.writerow([datetime.now(),"Down"])

def check_internet():
    print("Previous Status:")
    global prev_status
    if(ping("google.com")):
        if not prev_status:
            print("Status Changed")
            playsound('success.mp3')
            prev_status=True
        else:
            print("Status Unchanged")
        writer.writerow([datetime.now(),"Up"])

    else:
        if not prev_status:
            print("Status UnChanged")
        else:
            print("Status Changed")
            playsound('failure.mp3')
            prev_status=False
        
        writer.writerow([datetime.now(),"Down"])
    sleep(monitoring_interval)

while(1):
    check_internet()
