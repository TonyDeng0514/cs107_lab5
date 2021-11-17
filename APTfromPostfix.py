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

>>> print(eval(GenAPT('4 8 3 * +')))
28

>>> print(eval(GenAPT('4 8 + 3 *'))) 
36

>>> print(eval(GenAPT('7 8 + 3 2 + /')))
3

>>> print(eval(GenAPT('4')))
4

>>> print(eval(GenAPT('6 2 / 1 2 + *')))
9

>>> print(eval(GenAPT('8 2 / 2 2 + *')))
16

>>> print(eval(GenAPT('46 8 4 * 2 / +')))
62

"""
from stack107 import *
from BinTreeLinked import *

def GenAPT(exp: str) -> BT:
    assert type(exp) == type("a string")
    tokenlist = exp.split()
    nstack = stack107()

    for token in tokenlist:
        if token in '+-*/':
            right = nstack.top()
            nstack.pop()
            left = nstack.top()
            nstack.pop()
            temp = BT(token, left, right)
            nstack.push(temp)
        else:
            nstack.push(BT(token))
    return nstack.top()

def operate(op1, op2, operation):
    op1 = float(op1.root())
    op2 = float(op2.root())

    if op1 == int(op1):
        op1 = int(op1)
    if op2 == int(op2):
        op2 = int(op2)
    r = 0

    if operation == "+":
        r = op1+op2
        if r == int(r):
            r = int(r)
        return BT(r)
    elif operation == "*":
        r = op1*op2
        if r == int(r):
            r = int(r)
        return BT(r)
    elif operation == "-":
        r = op1 - op2
        if r == int(r):
            r = int(r)
        return BT(r)
    else:
        r = op1/op2
        if r == int(r):
            r = int(r)
        return BT(r)

def eval(x: BT):
    if x.leaf():
        return x.root()
    elif x.left().leaf() and x.right().leaf():
        return operate(x.left(), x.right(), x.root())
    elif not x.left().leaf():
        x.rep.ltree = eval(x.left())
        return eval(x)
    elif not x.right().leaf():
        x.rep.rtree = eval(x.right())
        return eval(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
