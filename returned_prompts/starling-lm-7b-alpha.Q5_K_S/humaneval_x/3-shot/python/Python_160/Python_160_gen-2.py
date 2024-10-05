    def evaluate(operators, operands):
        stack = []
        for op in operators:
            if op == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif op == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif op == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif op == '//':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            elif op == '**':
                a = stack.pop()
                b = stack.pop()
                stack.append(b ** a)
        return stack[0]

    return evaluate(operator, operand)


