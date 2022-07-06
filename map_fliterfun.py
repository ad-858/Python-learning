from functools import reduce
listt=[
    
    ("rice",50),
    ("sugar",60),
    ("Tea",10)
]
a=list(map(lambda x:x[1],listt))
print(a)
for i in a:
    print(i)
b=list(filter(lambda x:x[1]>30,listt))
print(b)  
l=[1,2,3,4]
c=reduce(lambda x,y:x+y,l)
print(c)

