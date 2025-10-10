class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)          
l1=int(input("Enter length of first rectangle:"))
b1=int(input("Enter breadth of first rectangle:"))

obj1=rectangle(l1,b1)
print("area of rectangle:",obj1.area())
print("perimeter of rectangle:",obj1.perimeter())
print()

l2=int(input("Enter length of second rectangle:"))
b2=int(input("Enter breadth of second rectangle:"))

obj2=rectangle(l2,b2)
print("area of rectangle:",obj2.area())
print("perimeter of rectangle:",obj2.perimeter())
print()

if obj1.area() > obj2.area():
    print("First Rectangle is greater")
elif obj1.area() < obj2.area():
    print("Second Rectangle is greater")
else:
    print("Both rectangle have equal area")
    

