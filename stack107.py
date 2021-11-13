"""
stack107: an implementation of a stack represented as Python list

>>> stk = stack107()
>>> assert stk.empty()
>>> stk.push("turing")
>>> stk.push("church")
>>> stk.push("shannon")
>>> assert not stk.empty()
>>> assert stk.top() == "shannon"
>>> stk.pop()
>>> assert stk.top() == "church"
>>> stk.pop()
>>> assert stk.top() == "turing"
>>> stk.pop()
>>> assert stk.empty()

"""

class stack107:
    def __init__(self):
        self.rep = []

    def empty(self):
        return self.rep == []

    def push(self, x):
        self.rep.append(x)

    def pop(self):
        assert not self.empty()
        self.rep.pop()

    def top(self):
        assert not self.empty()
        return self.rep[-1]

    def __str__(self):
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
