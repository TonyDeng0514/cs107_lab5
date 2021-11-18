"""
evaluating postfix expression with integers

test cases from
https://www.free-online-calculator-use.com/postfix-evaluator.html


>>> assert PostfixEval('4 8 3 * +') == 28
>>> assert PostfixEval('4 8 + 3 *') == 36
>>> assert PostfixEval('7 8 + 3 2 + /') == 3
>>> assert PostfixEval('4') == 4

more test cases!!!

>>> assert PostfixEval('6 2 / 1 2 + *') == 9
>>> assert PostfixEval('8 2 / 2 2 + *') == 16
>>> assert PostfixEval('46 8 4 * 2 / +') == 62
"""

from stack107 import *

def calculate(operator: str, op1: str, op2: str) -> str:
    assert operator in '+-*/'  # precondition, operator has to be one of the four basics.
    assert type(operator) == str  # preconditions, all inputs have to be str
    assert type(op1) == str
    assert type(op2) == str  
    
    # since we are only concerned with integers, changing them to integers is enough
    op1 = int(op1)
    op2 = int(op2)
    r = 0 # define a dummy output
    # different cases for operation

    if operator == '+':
        r = op1 + op2
    elif operator == '-':  # be careful here, the order of operation matters
        r = op1 - op2
    elif operator == '*':
        r = op1 * op2
    else:
        r = op2/op1    # order of operation matters
    
    if r == int(r):   # change to int if possible
        r = int(r)
    return str(r) #postcondition, the output has to be a string

def PostfixEval(exp: str)-> int:
    assert type(exp) == type("a string")  # precondition, input has to be a string

    NoStack = stack107()  # create an empty stack for further usage
    tokenList = exp.split()  # split the input, dilimeter as space.

    for token in tokenList:  # iterate through the list, push numbers, operate operations.
        if token in "+-*/":
            top = NoStack.top() # take the top
            NoStack.pop()       # pop the top
            top2 = NoStack.top() # take the new top
            NoStack.pop()  # pop the new top
            NoStack.push(calculate(token, top, top2)) # push the result as new new top
        else:
            NoStack.push(token)
    
    return int(NoStack.top()) # return the top
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
