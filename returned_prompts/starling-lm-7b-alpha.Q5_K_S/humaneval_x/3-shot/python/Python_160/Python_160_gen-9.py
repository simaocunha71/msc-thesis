    def evaluate(operand):
        stack = []
        for elem in operand:
            if type(elem) is int:
                stack.append(elem)
            else:
                if elem == '+':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 + val1)
                elif elem == '-':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
                elif elem == '*':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 * val1)
                elif elem == '//':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 // val1)
                elif elem == '**':
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 ** val1)
        return stack[0]

    return evaluate(operator + operand)


