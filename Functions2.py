def normalfunc():
    print("Hello Siva !")
    
def paramaterised(a,b):
    print(a,b)
    print("First Number is",a,"Second Number is ",b,"By Adding Them",(a+b))
    print(f"First Number is {a} Second Number is {b} and By Adding Them {a+b}")

def MultiParam(*pov):
    print(pov)
    print(pov[1])

def MultiKey(**pov):
    print(pov)
    print(pov["lname"],pov["fname"])

def AllowKey(*,name):
    print(name)


def AllowPos(name,/):
    print(name)

def AllowKeyPos(name,id,/,*,op,lp,):
    print(name)

def Returnstate(pol):
    return pol*2

normalfunc()
paramaterised(2,3)
# Multi Positioned Values
# Positioned Arguments
MultiParam(1,2,3,4)
# Multi keyWord values
# KeyWord Arguments
MultiKey(fname="Chanakya",lname="Manas")
# Only Allow Keywords
AllowKey(name="Chanakya")
# Only Allow Positions
AllowPos("Siva!!!!")
# Allow Both Keyword and Position
AllowKeyPos("Vikas",1,op="po",lp="pl")
# Return Func()
l=Returnstate(3)
# print(l)
i=0
while(i<l):
    print("Hello Viksas !")
    i+=1
    