n1=int (input("Enter the limit of first list:"))
list1=[]
for i in range(n1):
    num = int (input("Enter the numbers of first list:"))
    list1.append(num)
    
n2 = int (input("Enter the limit of second list:"))
list2=[]
for i in range(n2):
    num = int (input("Enter the numbers of second list:"))
    list2.append(num)
    
if len(list1) == len(list2):
    print("Both list have same length")
else:
    print("Both list have different length")

if sum(list1) == sum(list2):
    print("Both list have same sum")
else:
    print("Both list have different sum")

status=False
c=0
for j in list1:
    if j in list2:
        status=True
        c=c+1
if status==True:            
        print("Both list have common value:",c,"VALUES")
else:
    print("Both list not have common value:")
    

                     
                   
    
                   


    
