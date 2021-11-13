"""
evaluating postfix expression with integers

test cases from
https://www.free-online-calculator-use.com/postfix-evaluator.html


>>> assert PostfixEval('4 8 3 * +') == 28
>>> assert PostfixEval('4 8 + 3 *') == 36
>>> assert PostfixEval('7 8 + 3 2 + /') == 3
>>> assert PostfixEval('4') == 4
"""

from stack107 import *

def calculate(operator, op1, op2):
    assert operator in '+-*/'
    
    pass

def PostfixEval(exp: str)-> str:
    assert type(exp) == type("a string")

    pass
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
