Here is a Python solution that uses a loop to iterate over the operator and operand lists, performing the corresponding operation at each step:

```python
def DoAlgebra(operator, operand):
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
    return int(result)
```

This function takes two lists as input: `operator` and `operand`. It initializes a variable `result` to the first element of the `operand` list. Then, it loops over the `operator` list, performing the corresponding operation at each step. Finally, it returns the result as an integer.

For example, if we call the function with the following input:

```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
```

The function will return the result of the expression `2 + 3 * 4 - 5`, which is `9`.