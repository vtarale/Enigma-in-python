class Rotor:
    def __init__(self, gear, alphabets):
        self.alhpabets = alphabets
        self.gear = gear
        self.steps = 0

    def get(self, val):
        return self.alhpabets[val]

    def move(self):
        new_list = []
        i = 0
        for letter in self.alphabets:
            if i == 0:
                continue
            new_list.append(letter)
            i  = i + 1
        self.steps  = self.steps + 1
        new_list.append(self.alhpabets[0])
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
        if self.connections(char):
            return self.connections(char)
        return char

def move(r1, r2, r3):
    pass

def encrypt(string):
    rotor1 = Rotor(None, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rotor2 = Rotor(12, ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
    rotor3 = Rotor(2, ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
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
        c = pb.get(char)
        e = e + c
    return e