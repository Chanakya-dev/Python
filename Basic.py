# Assigning
p=90
p=" Siva"
b="Mani"
c=p+b

p=p+" Mani"
print(p)

# Assignin same Value to Multiple 
a=b=c=10
print(b)
print(a)
print(c)
a,b,c=5,4,3
print(a,b,c)
print(a+b+c)

# Casting
a=32
b=float(a)
print(a)
a=float(a)
print(a,b)
# a=a+" Babitha"
# print(a)

c=str(a)
print(c)
print(type(c))
c=c+" Charan"
print(c)
# d=int(c)
# print(d)
# d=32.0
# d=d+"Ravi"
# print(d)

#0 --> Flase
#!=0 ---> True
f=2
f=bool(f)
print(f)
# "" ->Flase
# !"" ->True
op=""
p=bool(op)
print(p)

# Input
name=input("Enter Your Name :")
print(name)

y=int(input("Enter your id :"))
z=float(input("Enter your score :"))