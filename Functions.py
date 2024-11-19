def funct():
    print("Hello World")

def funct1(a,b):
    print(f"This is Value {a} and This is Value {b}")

def funct2(*a):
    print(a[0])

def funct3(**a):
    print(a["lname"])

def funct4(a,/):
    print(a)

def funct5(*,b):
    print(b)

def functs(a,b):
    if a>b:
        return a-b
    else:
        return a+b

def functo(a):
    p=functs(5,3)
    a=p/a
    print(a)
    
funct5(b="Hello")

funct4("Chanakya")
funct3(fname="Chanakya",lname="Manas")
funct2(4,5,6)
funct1(2,3)
funct()
functo(2)
