# Here is a step-by-step guide to this problem:
# 1. We know that the length of the operator list is equal to the length of the operand list minus one.
# 2. So, let's create a function that takes a list of operators and a list of operands.
# 3. This function will return the result of the algebra expression.
# 4. We can achieve this by using the built-in reduce function in Python.

from operator import add, sub, mul, truediv, pow
from functools import reduce

def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
        "**": pow
    }
    return reduce(ops.get, operator, operand[0])


# Here is a test of the function:

if __name__ == "__main__":
    print(do_algebra(["+", "*", "-"], [2, 3, 4, 5]))








































