
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
    
    # 1. check if there are any non-operation in the operator list
    if len(operator) == 0 or not all(isinstance(el, str) for el in operator):
        return "ERROR: the operator list is invalid"
        
    # 2. check if length of operand list is greater than zero and there are no extra spaces
    if len(operand) < 1 or any([isspace(elem) for elem in operand]):
        return "ERROR: the operand list is invalid"    
    
    # 3. check if the length of operator list equals to the length of operand minus one
    if (len(operator) != len(operand)-1 or len(operator) < len(operand)):
        return "ERROR: the length of operator and operand lists are invalid"
    
    # 4. check what kind of value is in each position in the operator list
    for i, el in enumerate(operator):  
        if not (isinstance(el, str) or isinstance(el, int)):
            return "ERROR: invalid type in operation list"
    
    # 5. check length of operand - no