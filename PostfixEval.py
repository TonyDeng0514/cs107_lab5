"""
evaluating postfix expression with integers

test cases from
https://www.free-online-calculator-use.com/postfix-evaluator.html


>>> assert PostfixEval('4 8 3 * +') == 28
>>> assert PostfixEval('4 8 + 3 *') == 36
>>> assert PostfixEval('7 8 + 3 2 + /') == 3
>>> assert PostfixEval('4') == 4

>>> assert PostfixEval('6 2 / 1 2 + *') == 9
>>> assert PostfixEval('8 2 / 2 2 + *') == 16
>>> assert PostfixEval('46 8 4 * 2 / +') == 62
"""

from stack107 import *

def calculate(operator: str, op1: str, op2: str):
    assert operator in '+-*/'
    
    op1 = int(op1)
    op2 = int(op2)

    if operator == '+':
        return op1+op2
    elif operator == '-':
        return op2-op1
    elif operator == '*':
        return op1*op2
    else:
        return op2/op1

def PostfixEval(exp: str)-> int:
    assert type(exp) == type("a string")

    NoStack = stack107()
    tokenList = exp.split()

    for token in tokenList:
        if token in "+-*/":
            top = NoStack.top()
            NoStack.pop()
            top2 = NoStack.top()
            NoStack.pop()
            NoStack.push(calculate(token, top, top2))
        else:
            NoStack.push(token)
    
    return int(NoStack.top())
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
