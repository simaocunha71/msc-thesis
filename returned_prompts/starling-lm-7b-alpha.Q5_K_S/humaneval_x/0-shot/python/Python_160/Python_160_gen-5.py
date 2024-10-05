# Here are some ways to solve this problem.

# Method One: Using recursion
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
    # Base case
    if len(operator) == 1:
        return operand[0]
    else:
        # Recursive case
        operator_index = operator.index(operator[0])
        operand_index = operand.index(operand[0])

        left_operand = operand[operand_index]
        right_operand = operand[operand_index + 1]

        # Evaluate the expression
        if operator[0] == "+":
            return left_operand + right_operand
        elif operator[0] == "*":
            return left_operand * right_operand
        elif operator[0] == "-":
            return left_operand - right_operand
        elif operator[0] == "//":
            return left_operand // right_operand
        elif operator[0] == "**":
            return left_operand ** right_operand

# Method Two: Using stack data structure
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra