t1 = (1,2, [30, 40])
t2 = (1,2, [30, 40])

t1 == t2 # True
print(id(t1[-1]))
print(id(t2[-1]))

t1[-1].append(99)
# t1 = (1,2,[30,40,99])

t1 == t2 # False
# Altought the tuples are immutable we can change te list t[-1]

