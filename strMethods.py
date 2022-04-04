myStr="Hello, and welcome to my world!"
print(myStr.encode(encoding="ascii",errors="backslashes"))
print(myStr.endswith("!"))
str="H\te\tl\tlo"
print(str.expandtabs(12))