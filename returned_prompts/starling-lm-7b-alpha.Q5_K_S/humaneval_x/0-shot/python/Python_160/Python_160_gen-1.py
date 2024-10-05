To solve this problem, we can follow these steps:

1. Initialize a stack to store operands. We will use this stack to store the operands before the operations.

2. Initialize a variable `result` to 0. This variable will store the result of the expression.

3. Iterate through the `operator` list and the `operand` list simultaneously.

4. If the current item in the `operator` list is an addition (`+`), add the top two elements from the stack to the `result` and append the top element to the stack.

5. If the current item in the `operator` list is a subtraction (`-`), subtract the top element from the stack from the `result` and append the top two elements to the stack.

6. If the current item in the `operator` list is a multiplication (`*`), multiply the top two elements from the stack and append the result to the stack.

7. If the current item in the `operator` list is a floor division (`//`), divide the top element from the stack by the second top element and append the result to the stack.

8. If the current item in the `operator` list is an exponentiation (`**`), raise the top element from the stack to the power of the second top element and append the result to the stack.

9. If the current item in the `operator` list is not an operator, append it to the stack.

10. Repeat steps 4-9 until all the operators and operands have been processed.

11. The final result is stored in the `result` variable. Return this result.

Here is the Python code that implements the above steps:

```python
def do_algebra(operator, operand):
    stack = []
    result = 0
    for i, op in enumerate(operator):
        if op == '+':
            result += stack.pop() + stack.pop()
            stack.append(result)
        elif op == '-':
            result -= stack.pop()
            result += stack.pop()
            stack.append(result)
        elif op == '*':
            result = stack.pop() * stack.pop()
            stack.append(result)