import json

class main:
    def __init__(self):
        self.start()
        if self.loadType == 1:
            self.load(self.openfileName)
        elif self.loadType == 2:
            self.createNew(self.openfileName)
        self.File.close()

        self.loop()
        self.save()

    def start(self):
        print("load or new?")
        print("1. load")
        print("2. new")

        self.loadType = "1234567\899861231sssssss"
        while True:
            self.loadType = input("chose one(number)")
            if self.loadType == "1" or self.loadType =="2":
                break
            print("number!!!!")
        self.loadType = int(self.loadType)
        self.openfileName = input("name?")

    def createNew(self,name:str):
        self.File = open("./saves/"+name+".json","w")
        self.data = {"time":[0,0]}
        json.dump(self.data,self.File)

    def load(self,name:str):
        try:
            self.File = open("./saves/"+name+".json","r")
            self.data = json.load(self.File)
        except:
            print("error:can not find file!")
            import time
            time.sleep(3)
            import sys;sys.exit()

    def loop(self):
        self.count_fial()
        # print("1.fial")
        # print("2.new floor")
        # self.addType = "1234567\899861231sssssss"
        # while True:
        #     self.addType = input("chose one(number)")
        #     if self.addType == "1" or self.addType =="2":
        #         break
        #     print("number!!!!")
        # self.addType = int(self.addType)

        self.ifBack = False

    def count_fial(self):
        self.ifBack = False
        self.fialfloor = input("fail floor name or exit?")
        if self.fialfloor == "exit":
            self.ifBack = True
            return
        try:
            self.data[self.fialfloor] += 1
        except:
            print("can not find '"+self.fialfloor+"'floor")
            print("do you want create?")
            self.wantCreate = "1234567\899861231sssssss"
            while True:
                self.wantCreate = input("yes or no")
                if self.wantCreate == "yes" or self.wantCreate =="no":
                    break
            if self.wantCreate == "yes":
                self.data[self.fialfloor] = 1
            if self.wantCreate == "no":
                return
        
        self.addTime = "1234567\899861231sssssss"#minute
        self.addTimeIsInt = False
        while not self.addTimeIsInt:
            self.addTime = input("time minute:")
            self.addTimeIsInt = True
            try:
                self.addTime = int(self.addTime)
            except:
                print("number!!!!")
                self.addTimeIsInt = False
        try:
            self.data["time"][0]+= self.addTime
        except:
            self.data["time"] = [self.addTime,0]

        self.addTime = "1234567\899861231sssssss"#second
        self.addTimeIsInt = False
        while not self.addTimeIsInt:
            self.addTime = input("time second:")
            self.addTimeIsInt = True
            try:
                self.addTime = int(self.addTime)
            except:
                print("number!!!!")
                self.addTimeIsInt = False
        try:
            self.data["time"][1] += self.addTime
        except:
            self.data["time"] = [0,self.addTime]

    def save(self):
        with open("./saves/"+self.openfileName+".json","w") as self.File:
            json.dump(self.data,self.File)

main()