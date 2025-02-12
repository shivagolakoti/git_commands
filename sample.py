#print("lol")
#print("shiva lol")
a=10
b="z"
try:
    a+b
except TypeError:  
    print('type error')
else:
    print(a+b)
finally:
    print('exceptional handling') 
