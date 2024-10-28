```
def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list is not equal to length of operand list minus one.")
    if len(operand) < 2:
        raise ValueError("Operand list has less than two operands.")
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list contains non-integer or non-positive values.")

    def apply_operator(operator, operand):
        result = operand[0]
        for op, num in zip(operator, operand[1:]):
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "//":
                result //= num
            elif op == "**":
                result **= num
        return result

    return apply_operator(operator, operand)
```
This function first checks if the input lists are valid according to the problem description. If they are not, it raises a ValueError with a corresponding message. Then it defines a helper function `apply_operator` that iterates over the operator list and the operand list, applying each operator to the result. Finally, it calls `apply_operator` with the input lists and returns the result. This function should work correctly for any valid input.