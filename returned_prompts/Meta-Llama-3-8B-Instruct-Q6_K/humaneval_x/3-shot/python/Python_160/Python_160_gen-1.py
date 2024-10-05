    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list is not equal to the length of operand list minus one")

    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list has non-positive integers")

    if len(operand) < 2:
        raise ValueError("Operand list has less than two operands")

    if not all(x in '+-*///' for x in operator):
        raise ValueError("Operator list has non-basic algebra operations")

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


