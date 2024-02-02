import os.path
from tabulate import tabulate


class Container():
    def headers(self):
        print("\n")
        print("      ADD RECORD AND PRESS "+"q"+" TO CHANGE TO THE COLUMN                     ")

        self.key=""
        self.val=""
        self.dic={}
        print("\n")
        while (self.key!="q" or self.val=="Q"):
            self.key= input("Enter Headers: ")
            if self.key=="q"or self.val=="Q" :
                break
            self.dic[self.key]=[]
            print(tabulate(self.dic,headers="keys",tablefmt="github"))
            print("\n")

        for i in self.dic:
            self.val=""
            while(self.val!="q"):
                self.val=input("input "+str(i)+": ")
                if self.val=="q" or self.val=="Q":
                    break 
                self.dic[i].append(self.val)
                print("\n")
                print(tabulate(self.dic,headers="keys",tablefmt="github"))
                print("\n")

# tabulation
class Bundler(Container):
    def Bundle(self):
        self.headers()
        print("The resultant table is:")
        print('\n')
        print(tabulate(self.dic,headers="keys",tablefmt="github"))
        print("\n")

# Saving table in file
        if os.path.isfile('sheet.txt'):
            file=open('sheet.txt','a')
            file.writelines("\n"+"\n")
            file.writelines(tabulate(self.dic,headers="keys",tablefmt="github"))
            print("File saved ")
        else:
            file=open('sheet.txt','w')
            file.writelines("\n")
            file.writelines(tabulate(self.dic,headers="keys",tablefmt="github"))
            print("File saved")


obj=Bundler()
obj.Bundle()



    
