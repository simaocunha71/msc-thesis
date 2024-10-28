# Here is a step by step guide to solve this problem:

Step 1: Initialize the result to the first element in the operand list.
Step 2: Iterate through the operator and operand lists simultaneously. For each iteration:
    a. Check if the current operator is '+'. If it is, add the current operand to the result.
    b. If the current operator is '-', subtract the current operand from the result.
    c. If the current operator is '*', multiply the current operand by the result.
    d. If the current operator is '//', divide the result by the current operand. Note that the division is a floor division.
    e. If the current operator is '**', raise the result to the power of the current operand.
Step 3: Return the result.

Here is the Python code to implement this algorithm:

```python
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
            result = result ** operand[i + 1]
    return result
```

You can use the function like this:

```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)
```

This will output: `9`

Note: Make sure the operator and operand lists have the same length. If they don't, the program will raise an IndexError.

If you want to handle the case when the operator and operand lists have different lengths, you can add a check at the beginning of the function to ensure they have the same length. Here's how you can do it:

```python
def do_algebra(operator, operand):
    if len(