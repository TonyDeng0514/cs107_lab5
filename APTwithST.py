"""
Generating arithmetic parse tree from postfix expression

>>> print(GenAPT('4 8 3 * +'))
'4''+''8''*''3'

>>> print(GenAPT('6 2 / 1 2 + *'))
'6''/''2''*''1''+''2'

>>> print(GenAPT('8 2 / 2 2 + *'))
'8''/''2''*''2''+''2'

>>> print(GenAPT('46 8 4 * 2 / +'))
'46''+''8''*''4''/''2'

>>> print(GenAPT('4 8 3 * +').postorder())
'4''8''3''*''+'

>>> s = ST()
>>> s.set('a', 4)
>>> s.set('b', 8)
>>> s.set('c', 3)
>>> s.set('d', 7)
>>> s.set('e', 2)
>>> s.set('f', 6)
>>> s.set('g', 1)
>>> s.set('h', 46)

>>> print(eval(GenAPT('a b c * +'), s))
28

>>> print(eval(GenAPT('a b + c *'), s)) 
36

>>> print(eval(GenAPT('d b + c e + /'), s))
3

>>> print(eval(GenAPT('a'), s))
4

>>> print(eval(GenAPT('f e / g e + *'), s))
9

>>> print(eval(GenAPT('b e / e e + *'), s))
16

>>> print(eval(GenAPT('h b a * e / +'), s))
62

"""
from stack107 import *
from BinTreeLinked import *
from SymbolTable import ST


def GenAPT(exp: str) -> BT:
    assert type(exp) == type("a string")
    tokenlist = exp.split()
    nstack = stack107()

    for token in tokenlist:
        if token in '+-*/':
            right = nstack.top()  # take the first number
            nstack.pop()
            left = nstack.top()  # take the second number
            nstack.pop()
            temp = BT(token, left, right)  # operate and generate a new BT
            nstack.push(temp)  # add to top
        else:
            nstack.push(BT(token))  # push number as BT
    return nstack.top()

# this is operate when ST is a BST
def operate(op1, op2, operation, s: ST):
    if s.rep.lookup(op1.root()): # if the key is in ST
        op1 = s.get(op1.root()) # find value
    else:
        op1 = op1.root()  # directly use value
    if s.rep.lookup(op2.root()):
        op2 = s.get(op2.root())
    else:
        op2 = op2.root()

    op1 = float(op1) # transfer to float
    op2 = float(op2)

    r = 0  # dummy output

    if operation == "+":
        r = op1+op2
    elif operation == "*":
        r = op1*op2
    elif operation == "-":
        r = op1 - op2
    else:
        r = op1/op2

    if r == int(r):  # make every integer an integer
        r = int(r)
    return BT(r)

def eval(x: BT, s: ST):
    if x.leaf():
        return s.get(x.root()) # if leaf, get root
    elif x.left().leaf() and x.right().leaf(): # if both branches are leaves, operate
        return operate(x.left(), x.right(), x.root(), s)
    elif not x.left().leaf(): # if one is not leaf, keep moving
        x.rep.ltree = eval(x.left(), s)
        return eval(x, s)
    elif not x.right().leaf():  
        x.rep.rtree = eval(x.right(), s)
        return eval(x, s)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
