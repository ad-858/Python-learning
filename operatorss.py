# Arithmatic operators
from ast import operator


x=14
y=3
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x//y)
print(x**y)
# comparison operators
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
# logiacal operators
print(x>10 and y<5)
print(x>10 or y<5)
print (not(x>10 and y<5))
# identitiy operator
x=[5,0,89,100]
y=[5,0,89,100]
z=x
print(x is y)
print(x is z)
# membership operator
print(10 in x)
print(10 not in x)
# bitwise operator
x=5
y=3
print(x & y)
print(x | y)
print(x ^ y)
print(x ^ y)
print(x << y)
print(x >> y)