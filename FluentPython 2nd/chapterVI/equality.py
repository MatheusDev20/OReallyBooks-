me = {"name": "Matheus", "born": 1999}

copyOfMe = me

print(me is copyOfMe)
print(id(me)) # the id property of an object, never changes and in Cpython actually represents the
              # memory addres of that object as a integer
print(id(copyOfMe))
# This should change both objects, me and copyOfMe cause the reference is the same
copyOfMe['name'] = 'New Matheus'
print(me)

falseMe = {"name": "Matheus", "born": 1999}
# This should return true, cause uses the __eq__ implementation of the dict class
# and is not comparing the object reference but his properties
print(me == falseMe)
# The is keyword compares the references (id's) from objects
print(falseMe is me)

# is verus "=="

# The == operator compares the values of objects (the data they hold), while is compares their identities.

me == falseMe # => me.__eq__(falseMe)
