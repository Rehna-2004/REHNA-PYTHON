import csv
f=open("employ.csv","r")
content=csv.reader(f)
next (content)
for i in content:
    if int(i[2])>10:
        print(i)
