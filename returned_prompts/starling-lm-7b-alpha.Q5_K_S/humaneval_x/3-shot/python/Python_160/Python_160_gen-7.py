    def evaluate(operators, operands):
        """
        Recursively evaluate the expression given the remaining operators and operands.
        >>> evaluate(['+'], [3, 4])
        7
        >>> evaluate(['*'], [3, 4])
        12
        >>> evaluate(['//'], [10, 2])
        5
        """
        if not operators:
            return operands[0]
        elif len(operators) == 1:
            return evaluate(operators, operands)[operators[0]](operands[0], operands[1])
        else:
            left = evaluate(operators[:-1], operands[:-1])
            right = evaluate(operators[1:], operands[1:])
            return left[operators[0]](left, right)

    result = evaluate(operator, operand)
    if result[0] in ['+', '-']:
        return result[0](result[1], result[2])
    elif result[0] == '*':
        return result[1] * result[2]
    elif result[0] == '//':
        return result[1] // result[2]
    elif result[0] == '**':
        return result[1] ** result[2]


