
    def do_algebra(operator, operand):
        result = operand[0]
        for i in range(1, len(operand)):
            result = eval(f"{result} {operator[i-1]} {operand[i]}")
        return result

B:

    def do_algebra(operator, operand):
        result = operand[0]
        for i in range(1, len(operand)):
            result = result + operator[i-1] + operand[i]
        return result

C:

    def do_algebra(operator, operand):
        return eval(" ".join(f"{a} {b}" for a, b in zip(operand, operator)))
