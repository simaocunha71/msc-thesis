def do_algebra(operato, operand):
    result = operand[0]
    for i in range(len(operato)):
        op = operato[i]
        if op == "+":
            result += operand[i+1]
        elif op == "-":
            result -= operand[i+1]
        elif op == "*":
            result *= operand[i+1]
        elif op == "//":
            result //= operand[i+1]
        elif op == "**":
            result = pow(result, operand[i+1])
    return result

operato = ["+", "*", "-"]
operand = [2, 3, 4, 5]
result = do_algebra(operato, operand)
print(result)