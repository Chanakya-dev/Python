class Class12:
    branch=""
    def __init__(s,id,name):
        s.id=id
        s.name=name
    def __str__(self):
        return f"ID : {self.id} Name:{self.name}"
    def funct2(slf,num):
        return f"{slf.id*num}"
    
p1=Class12(1,"Chanakya")
p1.branch="CSE"
print(p1.id,p1.name,p1.branch)
print(p1)

p2=Class12(2,"Manas")
print(p2)
print(p2.funct2(34))