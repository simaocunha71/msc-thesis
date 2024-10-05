    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
    return result
    # Note: This code assumes that the input lists are valid and the operator list has at least one operator.
    #       It also assumes that the operand list has at least two operands. The function will not work correctly 
    #       if these assumptions are not met. For example, if the operator list is empty or the operand list 
    #       has only one element. You may want to add some error checking code to handle these cases. 
    #       Also, this code does not handle the case where the operator list has more than one operator of the same type. 
    #       For example, if the operator list is ['+', '+'] and the operand list is [2, 3]. In this case, 
    #       the function will return 5 instead of 5. You may want to add some code to handle this case correctly. 
    #       One way to do this is to use a stack to evaluate the expression. This would allow you to handle 
    #       operators of the same type correctly. 
    #       Another way to do this is to use a more advanced data structure, such as a parse tree, to represent 
    #       the expression. This would also allow you to handle operators of the same type correctly. 
    #       You can choose the approach that is most suitable for your needs. 
    #       For example, you could use a stack to evaluate the expression, or you could use a parse tree to 
    #       represent the expression and then evaluate it using a stack. 
    #       You could also use a combination of these approaches. 
    #       For example, you could use a stack to evaluate the expression, and then use a parse tree to 
    #       represent the result. 
    #       You could also use a combination of these approaches. 
    #       For example, you could use a stack to evaluate the expression, and then use a parse tree to 
    #       represent