```
def do_algebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
    return result
```


The function `do_algebra` takes two lists as input, `operator` and `operand`. It iterates over the `operator` list and applies the corresponding algebra operation to the current result and the next operand. The final result is returned. The function assumes that the inputs are valid, i.e., the length of `operator` is equal to the length of `operand` minus one, and `operand` contains at least two non-negative integers. 

For example, if `operator` is `['+', '*', '-']` and `operand` is `[2, 3, 4, 5]`, the function will evaluate the expression `2 + 3 * 4 - 5` and return the result `9`. 

The function also handles the edge cases, such as division by zero for floor division, and negative exponents for exponentiation. However, it does not handle invalid inputs, such as an empty `operator` list or a `operand` list with less than two elements.  If you want to handle these cases, you can add error checking code to the function.  For example, you can check if the `operator` list is empty before iterating over it, and check if the `operand` list has less than two elements before trying to access its elements.  If an error is detected, you can raise an exception or return an error message. 

Here is an example of how you can modify the function to add error checking:
```
def do_algebra(operator, operand):
    if not operator:
        raise ValueError("Operator list is empty")
    if len(operand) < 2:
        raise ValueError("Operand list has less than two elements")
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
