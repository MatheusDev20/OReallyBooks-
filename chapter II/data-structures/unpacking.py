import os

# parallel assignement
lax_coordinates = (33.942, -118.408056)

latitude, longitude = lax_coordinates

print(latitude, longitude)

a = 10
b = 20

# change variables values without aux with unpacking
b, a = a, b 

t = (20, 8)
divmod(*t)
# (2,4)
quotient, remainder = divmod(*t)

_, filename = os.path.split('/home/matheus/projects') # unpacking the tuple that is returned from os.path.split()
print(filename)

# * to grab excess items
a, b,  *rest = range(5) # this is like spread operator.
print(rest)


a, b, *rest = ('A', 'B', 3, [4, 5, 'D'])
print(rest)


# Nested Unpacking 
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def func():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

func()
