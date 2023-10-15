import json

fileName = input("ouput fial name")

try:
    f = open("./saves/"+fileName + ".json","r")
except:
    print("error:can not find file!")
    import time
    time.sleep(3)
    import sys;sys.exit()

data = json.load(f)
wf = open("./outputs/"+fileName + ".txt","w")

wf.write(""" 
time:
{}m{}s
fails:\n""".format(data["time"][0],data["time"][1]))

fails = []
for name in data:
    if name != "time":
        wf.write("floor" + name + ":" + str(data[name])+"\n")

f.close()
wf.close()