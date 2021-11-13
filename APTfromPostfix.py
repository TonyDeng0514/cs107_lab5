"""
Generating arithmetic parse tree from postfix expression

>>> print(GenAPT('4 8 3 * +'))
'4''+''8''*''3'

>>> print(GenAPT('4 8 3 * +').postorder())
'4''8''3''*''+'

"""
from stack107 import *
from BinTreeLinked import *

def GenAPT(exp):
    assert type(exp) == type("a string")

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
