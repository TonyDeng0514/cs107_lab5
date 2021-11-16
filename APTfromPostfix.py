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
    op1 = float(op1)
    op2 = float(op2)
    if operation == "+":
        return str(op1+op2)
    elif operation == "*":
        return str(op1*op2)
    elif operation == "-":
        return str(op1 - op2)
    else:
        return str(op1/op2)

def eval(x: BT):
    if x.left() in "+-*/":
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
