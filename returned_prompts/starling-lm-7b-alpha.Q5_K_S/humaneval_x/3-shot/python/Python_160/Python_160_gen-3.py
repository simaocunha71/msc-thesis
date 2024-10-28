    def evaluate(operand, operator):
        stack = []
        for elem in operand:
            if type(elem) == int:
                stack.append(elem)
            else:
                if len(stack) < 2:
                    raise ValueError("Stack is not long enough")
                if operator == "+":
                    stack[-2] += stack[-1]
                    stack.pop()
                elif operator == "-":
                    stack[-2] -= stack[-1]
                    stack.pop()
                elif operator == "*":
                    stack[-2] *= stack[-1]
                    stack.pop()
                elif operator == "/":
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
                elif operator == "**":
                    stack[-2] = int(pow(stack[-2], stack[-1]))
                    stack.pop()
                else:
                    raise ValueError("Unknown operator")
        return stack[0]

    return evaluate(operand, operator)



