l=int(input("Enter the limit:"))
list=[]
for i in range(l):
    number=int(input("Enter the number:"))
    if (number>100):
        list.append('over')
    else:
        list.append(number)
print(list)        

     
    
