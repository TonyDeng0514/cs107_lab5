"""
Symbol Table represented as a Python dictionary

>>> t = ST()       # empty symbol table
>>> t.set('x', 5)
>>> t.set('y', 3)
>>> t.set('z', t.get('x'))
>>> assert t.get('z') == t.get('x')
>>> assert not t.get('z') == t.get('y')
>>> print(t)
{'x': 5, 'y': 3, 'z': 5}
"""

class ST:                   # symbol table
    def __init__(self):             # construct an empty ST
        self.rep = {}

    def set(self, where, what):     # setter (mutator)
        pass

    def get(self, where):           # getter (accessor)
        pass

    def __str__(self):              # abstract to text
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
