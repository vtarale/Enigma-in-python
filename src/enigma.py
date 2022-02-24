class Rotor:
    def __init__(self, gear):
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.gear = gear
        self.steps = 0

    def get(self, val):
        return self.alphabets[val]

    def move(self):
        new_list = []
        i = 0
        for letter in self.alphabets:
            if i == 0:
                continue
            new_list.append(letter)
            i  = i + 1
        self.steps  = self.steps + 1
        new_list.append(self.alphabets[0])
        self.alhpabets = new_list

class PlungeBorad:
    def __init__(self):
        self.connections = {
            'a':'z',
            'b':None,
            'c':None,
            'd':None,
            'e':None,
            'f':None,
            'g':None,
            'h':None,
            'i':None,
            'j':None,
            'k':None,
            'l':None,
            'm':None,
            'n':None,
            'o':None,
            'p':None,
            'q':None,
            'r':None,
            's':None,
            't':None,
            'u':None,
            'v':None,
            'w':None,
            'x':'y',
            'y':None,
            'z':None
        }
    
    def get(self, char):
        if self.connections[char]:
            return self.connections[char]
        return char

def move(r1, r2, r3):
    r1.move()
    if r2.steps % 26 == r2.gear:
        r2.move()
        if r3.steps % 26 == r3.gear:
            r3.move()

def encrypt(string):
    rotor1 = Rotor(None)
    rotor2 = Rotor(12)
    rotor3 = Rotor(2)
    pb = PlungeBorad()
    e = ""
    for char in string:
        start = 3
        c = pb.get(char)
        move(rotor1, rotor2, rotor3)
        c = rotor1.get(start)
        c = rotor2.get(start)
        c = rotor3.get(start)
        start = 26-start
        c = rotor3.get(start)
        c = rotor2.get(start)
        c = rotor1.get(start)
        c = pb.get(c)
        e = e + c
    return e

hello = encrypt("egg")
print(hello)