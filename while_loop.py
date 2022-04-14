i=1
a=0
while i<=100:
    a=a+i
    i=i+1
print(a)

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i=0
while i<len(lst):
    if lst[i]==100:
        print("the index of 100 is :"+ " "+str(i))
    i=i+1
