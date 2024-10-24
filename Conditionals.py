a=2
b=5
d=a+b
d=a-b
d=b%a
d=b/a
d=b//a
d=b*a
d=b**a
print(d)

# 5//2=2 --- 1
# 2//2=1 --- 0
# 1//2=1 --- 1


# 3//2=1 --- 1
# 1//2=1 --- 1
# 0101
# 0011
# -------

# 0001
# 0 * 2^3
# 0 * 2^2
# 0 * 2^1
# 1 * 2^0
# 1

# 0101
# 0  2^3 = 0
# 1  2^2 = 4
# 0  2^1 = 0
# 1  2^0 = 1
# ---------------------
#          5


# &  
# | 

a = 5  # (binary: 0101)
b = 3  # (binary: 0011)
# 0001
# 0010
# 1000
result = a & b  # (binary: 0001) => decimal: 1
print(result)  # Output: 1



# Assignment Operators
a=20
a=a+2
a+=2
a&=3

a=30
b=30
c=a
if c is b:
    print("Same")