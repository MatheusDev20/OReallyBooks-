# Pass a variable number of arguments in a function


from typing import Mapping

def dump(**kwargs):
    return kwargs['cpf']

params = {"cpf": '14032063680', "number": 1}
print(dump(**params))

def add_numbers(x,y ,z):
    return x + y + z

print(add_numbers(3,5,7))

def add_numbers_with_args(*numbers):
    # numbers are pass as a tuple
    sum = 0
    print(type(numbers))
    for n in numbers:
        sum += n

    return sum

print(add_numbers_with_args(3,5,6,7,1,3,321,2))

def intro(**data):
    print(f"Data type of a argument is{type(data)}")
    for k,v in data.items():
        print( "{} is {} ".format(k,v))

intro(**{'cpf': '123456789'})

# ** can only me used in dictionarys
