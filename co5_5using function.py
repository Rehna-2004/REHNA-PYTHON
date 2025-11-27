import csv
#input dictionary using user input method
data={}
n=int(input("Enter the limit"))
for i in range(n):
    key=input("Enter the key")
    val=input("Enter the value")
    data[key]=val
print(data)

def cwrite():
#csv writing
    f=open("dictdata.csv","w",newline='')
    content=csv.writer(f)
    content.writerow(data.keys())
    content.writerow(data.values())
    f.close()
def cread():    
#csv reading
    f1=open("dictdata.csv","r")
    cont=csv.reader(f1)
    for i in cont:
        print(i)
    f1.close()    
cwrite()
cread()
