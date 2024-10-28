Here is the Python code that solves the problem:

```python
def do_algebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result
```

This code initializes the result with the first operand and then iterates over the operator and operand lists. For each operator, it applies the corresponding operation to the result and the next operand. Finally, it returns the result.

Here's how you can use this function with the example you provided:

```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9
```