import copy
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(f' Bus 1 Reference id -> ${id(bus1)}\n Bus 2 Reference id -> ${id(bus2)}\n Bus 3 Reference id -> ${id(bus3)}')

bus1.drop('Bill')
print(bus2.passengers)

