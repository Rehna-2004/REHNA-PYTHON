import csv
f=open("studd1.csv","w",newline="")
content=csv.writer(f)
for i in range(2):
    name=input("Enter the name")
    age=int(input("Enter the age"))
    mark=float(input("Enter the mark"))
    l=[name,age,mark]
    content.writerow(l)
f.close()

f1=open("studd1.csv","r")
content=csv.reader(f1)
for i in content:
    print(i)

    
    
