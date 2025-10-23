class appooppan:
    
    def __init__(self,name):
        self.grandname=name
    def displaydetail(self):
        print("NAME IS : ",self.grandname)
        
        
class achan(appooppan):
        def __init__(self,gname,achanname,bi):
            super().__init__(gname)
        
            self.achanname=achanname
            self.bike=bi
            
        def displaydetail(self):
            super().displaydetail()
            print("achan name IS : ",self.achanname)
            print("bike IS : ",self.bike)
            
class kochumon(achan):
        
            def __init__(self,grantname,achaname,bi,sonname,phone,car):
                super().__init__(grantname,achaname,bi)
                self.s=sonname
                self.p=phone
                self.c=car
        
           
        
            def displaydetail(self):
                super().displaydetail()
                print("kochumonte name : ",self.s)
                print("phone : ",self.p)
                print("car : ",self.c)

appoopantename=input("enter appoppas name")
achantename=input("enter achans name")
achantebike=input("enter appans bike")
kochmonname=input("enter  kochumon name")
phone=int(input("enter  kochumon phon"))
car=input("enter  kochumon caR")

kochumonobj=kochumon(appoopantename,achantename,achantebike,kochmonname,phone,car)

kochumon.displaydetail()

