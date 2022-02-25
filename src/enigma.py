import random

class Rotor1:
    def __init__(self):
        self.rotor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def move(self):
        temp = self.rotor[0]
        self.rotor = self.rotor[1:]
        self.rotor.append(temp)
    
    def randomize(self):
        temp = random.randint(0, 26)

        for i in range(temp):
            self.move()
        
    def get(self, val): #value is till 0-25
        return self.rotor[val]

class Rotor2(Rotor1):
    def check(self):
        if self.rotor[0] == 'b':
            return True
        return False

class Rotor3(Rotor1):
    def check(self):
        if self.rotor[0] == 'z':
            return True
        return False
    
    def get_back(self):
        return self.rotor[len(self.rotor)-1], len(self.rotor)-1