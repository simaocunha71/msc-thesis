    def calculate(op1, op2, oper):
        if oper == "+":
            return op1 + op2
        elif oper == "-":
            return op1 - op2
        elif oper == "*":
            return op1 * op2
        elif oper == "//":
            return op1 // op2
        elif oper == "**":
            return op1 ** op2

    result = operand[0]
    for idx in range(1, len(operator)):
        oper = operand[idx]
        oper1 = operand[idx - 1]
        oper2 = result
        op = operator[idx]
        result = calculate(oper1, oper2, op)
    return result


