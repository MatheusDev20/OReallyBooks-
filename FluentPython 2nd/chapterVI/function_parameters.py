# The paremeters gets a copy of the reference from the original element
def f(a,b):
    a +=b
    return a

x = 1
y = 2
# a,b get copy of reference to the elements (1,2)
print(f(x,y))

# if the element is a muttable object (list) , he can be changed by the funcion
x = [1,2,3]
y = [4,5,6]
print(f(x,y))
print(x)
# [1,2,3,4,5,6] the x object was changed inside the function "f" because the parameter was carryin
# his reference


