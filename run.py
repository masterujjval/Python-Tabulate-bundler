import os.path
from tabulate import tabulate
print("\n")
print("      ADD RECORD AND PRESS "+""q""+" TO CHANGE TO THE COLUMN                     ")

key=""
val=""
dic={}

while (key!="q" or val=="Q"):
    key= input("Enter Headers: ")
    if key=="q"or val=="Q" :
        break
    dic[key]=[]
    print(tabulate(dic,headers="keys",tablefmt="github"))
    print("\n")

for i in dic:
    val=""
    while(val!="q"):
        val=input("input "+str(i)+": ")
        if val=="q" or val=="Q":
            break 
        dic[i].append(val)
        print("\n")
        print(tabulate(dic,headers="keys",tablefmt="github"))
        print("\n")

# tabulation
print("The resultant table is:")
print('\n')
print(tabulate(dic,headers="keys",tablefmt="github"))
print("\n")

# Saving table in file
if os.path.isfile('sheet.txt'):
    file=open('sheet.txt','a')
    file.writelines("\n"+"\n")
    file.writelines(tabulate(dic,headers="keys",tablefmt="github"))
    print("File saved ")
else:
    file=open('sheet.txt','w')
    file.writelines("\n")
    file.writelines(tabulate(dic,headers="keys",tablefmt="github"))
    print("File saved")






    
