def vikas():
    print("Hello Vikas")

def charan(name):
    print(f"Hello {name}")
def func(id,name,fee,course):
    print(f"ID: {id}, Name: {name}, Fee {fee}, course: {course}")

def func1(*num):
    print( "This is Number ", num[2])
    

vikas()
charan("Charan")
func(1,"Charan",34000,"Python")
func1(1,2,3,4,5,6,7)


def funckey(name):
    print(f"Hi {name}")


def funckey1(**keys):
    print("name:", keys["lname"])


funckey(name="Siva")
funckey1(fname="Chanakya",lname="Manas")


def function1(name,/):
    print(f"Your name {name}")


def function2(name):
    print(f"Your name {name}")

function2("Chanakya")
function2(name=" Manas")   


function1("Chanakya") 
# function1(name=" Manas")

print("Key Argument Based ------")
def keyfunct1(*,name):
    print(f"Hello {name}")


print("Normal Function")
function2("Chanakya")
function2(name="Chanakya")

keyfunct1(name="Chanakya")
# keyfunct1("Chanakya")

def combination(id,name,/,*,course):
    print(f"ID {id} Name {name} course {course}")

combination(1,"Chanakya",course="Python")
# combination(id=1,name="Chanakya",course="Python")