    def calculate(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "//":
            return a // b
        elif op == "**":
            return a ** b
        else:
            raise ValueError("Invalid operator")

    operators = operator
    operands = operand

    stack = []

    for i, op in enumerate(operators):
        if op == "+" or op == "-" or op == "*" or op == "//" or op == "**":
            stack.append(op)
        else:
            stack.append(int(op))

    result = stack[0]

    for i, op in enumerate(operators):
        if op == "+" or op == "-" or op == "*" or op == "//" or op == "**":
            result = calculate(result, stack[i + 1], op)
        else:
            stack.pop(i + 1)

    return result


