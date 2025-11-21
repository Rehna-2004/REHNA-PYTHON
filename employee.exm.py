import csv
f=open("emp new.csv","a",newline='')
content=csv.writer(f)
limit=int(input("Enter the limit:"))
for i in range(limit):
    name=input("Enter the name:")
    empid=int(input("Enter the id:"))
    salary=int(input("Enter the salary:"))
    l=[name,empid,salary]
    content.writerow(l)
f.close()
   

   
f1=open("emp new.csv","r")
content=csv.reader(f1)
next(content)
for i in content:
    if int(i[2])>10000:
        print(i)
f1.close()

