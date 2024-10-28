    from functools import reduce

    def multi_op(operands, operator):
        if len(operands) == 1:
            return operands[0]
        else:
            if operator == "+":
                return operands[0] + operands[1]
            elif operator == "-":
                return operands[0] - operands[1]
            elif operator == "*":
                return operands[0] * operands[1]
            elif operator == "//":
                return operands[0] // operands[1]
            elif operator == "**":
                return operands[0] ** operands[1]

    result = reduce(multi_op, zip(operator, operand))

    return result


