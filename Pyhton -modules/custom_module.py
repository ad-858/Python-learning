# we can call thr custome module using a keyword import
import my_module
print(my_module.add(5,15))
print(my_module.sub(25,15))
print(my_module.mul(25,15))
print(my_module.div(25,5))
# you ca n create an alis using as keyword

import my_module as my
print(my.add(10,10))
# you can also call also specific parts of a module using from keyword
from my_module import add
print(my_module.add(40,40))
#  dir() function gives you the list of all variables,functions,files and everything used in module(custom or built in module)
print(dir(my_module))
# to find the path of module
import sys
print(sys.path)
