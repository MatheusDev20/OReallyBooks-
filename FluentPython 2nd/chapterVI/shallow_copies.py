# A Shallow copy, creates another object, but the referecens of the items is still the same.

# Copies in Python are Shallow by default

l1 = [3, [66, 55, 44], (7, 8, 9)]
# Generates a shallow copy of list one -> (l2)
l2 = list(l1)  
# Append 100 to l1 has no effect on l2 cause they are different object 'l1 is not l2 == True'
l1.append(100)
# Append value 55 on a muttable object l[1]
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

c1 = ['MyName', [1,2,3], (4,5,6)]

c2 = c1
print(c1 is c2) # True
c2[1].append(99)
print(c1[1])
