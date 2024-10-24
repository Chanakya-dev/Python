# Conditional Statements
a=80
b=60

if a>b:
    b+=10
    print(b,"B is Increased")
if a>b:
    b+=10
    print(b," B is Increased Elif ")
else:
    print("Both are Equal")

print("A is Great")if a>b else print("B is Great")if b>a else print("Equal") 

for shiva in range(2,8,2):
    print(shiva)
name="Siva"

for x in name:
    print(x)

for x in range(2,10):
    if x == 5:
        continue
    print(x)
x=0 
while(x in range(6)):
    print(x)
    x+=1


for x in range(2,10):
    print(x)

for x in range(6,1):
    print(x)
    x=0 
x=6
while(x>0):
    print(x)
    x-=1

p=2
q=3
if p!=q:
    print("Not Equal")
    if p>q:
        q=p
        print(q,"If Bolck")
    elif q>p:
        p=q
        print(p," Elif Block")
    