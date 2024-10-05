```python
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(1, len(operand)):
        expression += ' ' + operator[i-1] + ' ' + str(operand[i])
    return eval(expression)

# Test
operator = ['+', '*', '-']
array = [2, 3, 4, 5]
print(do_algebra(operator, array))  # Output: 9
```

This solution builds the algebraic expression as a string and then uses the `eval` function to evaluate it.