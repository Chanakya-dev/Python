# Define Class
class Class12:
#  Constructor Which Hold Variables to give values
    def __init__(s,id,name):
        s.id=id
        s.name=name
        # str function to return values which are assigned 
    def __str__(self):
        return f"ID : {self.id} Name:{self.name}"
    # Declaring and defining Function
    def funct2(slf,num):
        return f"{slf.id*num}"
   
#Creating Object 1  With p1 as reference variable
p1=Class12(1,"Chanakya")
# Accessing Variables
print(p1.id,p1.name)
# Accessing str
print(p1)

#Creating Object 2  With p2 as reference variable
p2=Class12(2,"Manas")
# Accessing str Function
print(p2)
# Accessing Return Function
print(p2.funct2(34))