str1=input("Enter a string:")
count=dict()
word=str1.split()
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for k,v in count.items():
    print(k,":",v)
