

def funct1():
    print("Normal Func()")

def funct2(course,name,id):
    print("My name is ",name,"My Id is",id,"My Course is ",course)
    print(f"I Have an ID : {id} and My name is {name} I Have Selected Course {course}")

funct1()
# Key Word Argument
funct2(course="Python",name="Chanakya",id=1)
# Positioned Arguments
funct2("Python","Chanakya",1)

def funct3(*args):
    print(f" This is My  Third No {args[2]}")

funct3(1,2,3,4,5)

    

def keyfunc3(**args):
    print(f"Hello {args["name"]} and my age is {args["age"]}")

keyfunc3(name="Chanakya",age=23)

def functiPosit(name,/):
    print(f" Hello {name}")

functiPosit("Chanakya")
# functiPosit(name="Chanakya")

def funckey(*,ui):
    print(f"Thi is my desg {ui}")

funckey(ui="Developer")
# funckey("Developer")

def funckey1(*, a, b, **ui): 
    print(f"This is my design: {ui}")
    print(f"Required parameters: a = {a}, b = {b}")

funckey1(a=1, b=2, c="test", d=4)

    

