
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
    
    if len(operator) < 1:
        print "Error 0"
        return
    # Get the length of two lists and compare them to prevent the program from crashing.
    op_len = len(operator) - 1
    ops_len = len(operand) + op_len
    
    result = []
    for i in range(ops_len):
        try:
            val = str(eval(str(i)))
        except ValueError,e:
            print "Error 1"
            return
        
        if e == 'float object':
            continue
        
        result.append(eval(str(val)))
    
    return str(result)

if __name__ == '__main__':
    operators = ['**', '*', '-']
    operands = [3,5]
    
    print do_algebra(*operators, *operands)