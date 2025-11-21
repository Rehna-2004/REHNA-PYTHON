class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("name:",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super(). __init__(name)
        self.title=title
        self.author=author
    def display(self):
        super(). display()
        print("title:",self.title)
        print("author:",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,page):
        super(). __init__(name,title,author)
        self.price=price
        self.page=page
    def display(self):
        super(). display()
        print("price:",self.price)
        print("page:",self.page)
       
pub_name=input("Enter the Publisher Name:")
title=input("Enter the title Name:")
author=input("Enter the Author:")
price=int(input("Enter the price"))
page=int(input("Enter the No of Pages:"))

book=Python(pub_name,title,author,price,page)
book.display()
