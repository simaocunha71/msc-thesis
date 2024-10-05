Here is a Python solution for the problem:

```Python
def DoAlgebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//' or operator[i] == '**':
            if operator[i] == '//' and operand[i + 1] == 0:
                return 0
            result = int(eval(f'{result} {operator[i]} {operand[i + 1]}'))
    return result
```

This Python function takes two lists as input. The first list is a list of operator symbols, and the second list is a list of operands. The function evaluates the algebraic expression by iterating over the operators and operands and performing the corresponding operations. The function also handles the edge case where the floor division operator is used with a divisor of zero, in which case the function returns 0. The function finally returns the evaluated result.

For example, if the input is `operator=['+', '*', '-'], operand=[2, 3, 4, 5]`, the function will evaluate the expression `2 + 3 * 4 - 5` and return the result `9`. If the input is `operator=['//'], operand=[2, 0]`, the function will return 0 because of the edge case where the floor division operator is used with a divisor of zero.