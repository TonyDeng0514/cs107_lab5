"""
adapted from https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html


>>> assert infixToPostfix("A * B + C * ( D + E )") == 'A B * C D E + * +'
>>> assert infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -'
>>> assert infixToPostfix("7") == '7'
"""

from stack107 import *

def infixToPostfix(infixexpr: str)-> str:
    assert type(infixexpr) == type("a string")

    # a dictionary with precedence values
    prec = {}
    prec["*"] = prec["/"] = 3
    prec["+"] = prec["-"] = 2
    prec["("] = 1

    opStack = stack107()        # stack for scratch work (matching operands)
    postfixList = []            # holds the result
    tokenList = infixexpr.split()   # tokenize: now a list of tokens

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
