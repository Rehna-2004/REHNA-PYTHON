dic={}
l=int(input("Enter the limit:"))
for i in range(l):
    k=input("Enter the key:")
    val=int(input("Enter the value:"))
    dic[k]=val
print("In ascending order")
print(dict(sorted(dic.items())))
print("In descending order")  
print(dict(sorted(dic.items(),reverse=True)))

    
    
