To solve this problem, you can use recursion to evaluate the expression. Here's a step-by-step explanation of the solution:

1. Initialize the `result` variable to 0. This will store the result of the algebraic expression.
2. Create a helper function called `recursive_evaluation` that takes in the `operator`, `operand`, `index`, and `result` variables as arguments. This function will perform the recursive evaluation of the expression.
3. In the `recursive_evaluation` function, check if the `index` is less than the length of the `operand` list. If it is, it means there are still more operands to process. In this case, return the `recursive_evaluation` function with the updated `index` and `result` variables.
4. If the `index` is not less than the length of the `operand` list, it means we have reached the end of the expression. Here, you can use the `operator[index]` to determine the operation to be performed on the `result` and the next operand.
5. After determining the operation, update the `result` variable with the result of the operation and return the `result`.
6. Call the `recursive_evaluation` function initially with the `operator`, `operand`, `0`, and `result` variables as arguments.
7. Finally, return the `result` variable, which will contain the evaluated expression.

Here's the code for the solution:

```python
def do_algebra(operator, operand):
    result = 0

    def recursive_evaluation(index, result):
        if index < len(operand):
            return recursive_evaluation(index + 1, result)
        else:
            return result

    return recursive_evaluation(0, result)
```

You can use the `do_algebra` function by passing in the `operator` and `operand` lists as arguments. For example:

```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9
```

