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
    assert type(exp) == type("a string")  # precondition, input has to be a string
    tokenlist = exp.split()  # split the string with delimiter as space
    nstack = stack107()  # empty stach for future purpose

    for token in tokenlist:
        if token in '+-*/':
            right = nstack.top() # take the top
            nstack.pop()  # pop the top
            left = nstack.top()  # take the new top
            nstack.pop()  # pop the new top
            temp = BT(token, left, right)  # creat a BT using the top and new top
            nstack.push(temp)  # push the BT as the new new top
        else:
            nstack.push(BT(token))  # push numbers as a leaf
    return nstack.top()

def operate(op1: BT, op2: BT, operation) -> BT:  # help function
    op1 = float(op1.root())  # precondition op1 and op2 are BT
    op2 = float(op2.root())

    if op1 == int(op1):  # changing the integer ones to integer type
        op1 = int(op1)
    if op2 == int(op2):
        op2 = int(op2)
    r = 0  # dummy output
    # different methods for different operations
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

def eval(x: BT):
    if x.leaf(): # if is a leaf, return the root.
        return x.root()
    elif x.left().leaf() and x.right().leaf(): # if both branches are leaves, operate
        return operate(x.left(), x.right(), x.root())
    elif not x.left().leaf(): # if one of them is not a leaf, recursivly run again
        x.rep.ltree = eval(x.left())
        return eval(x)
    elif not x.right().leaf(): # same as above
        x.rep.rtree = eval(x.right())
        return eval(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
