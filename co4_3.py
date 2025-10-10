class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)
    def __lt__(self,second):
       if self.area()<second.area():
          return True
       else:
          return False

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
obj1.area()
obj2.area()

if obj1 > obj2:
    print("First Rectangle is greater")
elif obj1 < obj2:
    print("Second Rectangle is greater")
else:
    print("Both rectangle have equal area")
    
    
