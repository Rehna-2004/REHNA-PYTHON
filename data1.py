import csv
f=open("data.csv","r")
content=csv.reader(f)
f=int(input("Enter the number:"))
for i in content:
 print(i[f])
