#write a program to read a file line by line and store it into a list

file=open("sree.txt","r")
content=file.readlines()
linelist=[]
for i in content:
    print(i)
    line=i.strip()
    linelist.append(line)
print(linelist)
file.close()
