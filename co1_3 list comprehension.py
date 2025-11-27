#Generate positive list of numbers from a given list of integers.
#n=[-5, 3, 0, 8, -2, 7, -1]
#pn=[i for i in n if i > 0]
#print(pn)


#Square of N numbers
#n=int(input("Enter the numbers:"))
#v=[i*i for i in range(n)]
#print(v)      


#Form a list of vowels selected from a given word
w=input("Enter the word:")
v=[i for i in w if i.lower() in "aeiou"]
print("Vowels in the word:",v)
