# randint():generate a random number between the range given(both numbers are included)
import random
x=random.randint(3,6)
print(x)
x=random.randrange(3,6) #6 is not included
print(x)
x=random.random()#random float 0-1
print(x)
x=random.choices((10,23,35))
print(x)
x=([10,23,35,40])
random.shuffle(x)
