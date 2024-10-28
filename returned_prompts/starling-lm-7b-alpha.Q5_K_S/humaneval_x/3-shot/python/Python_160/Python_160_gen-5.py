    def compute_expression(operators, operands):
        stack = []
        for i, op in enumerate(operators):
            if op == '+':
                stack.append(operands[i] + operands[i+1])
            elif op == '*':
                stack.append(operands[i] * operands[i+1])
            elif op == '-':
                stack.append(operands[i] - operands[i+1])
            elif op == '//':
                stack.append(operands[i] // operands[i+1])
            elif op == '**':
                stack.append(operands[i] ** operands[i+1])

        return stack[0]

    return compute_expression(operator, operand)


