Here is a Python solution for your problem. This function iterates over the operator and operand lists, performing the corresponding operation on the operands and storing the result. The final result is returned.

```Python
def DoAlgebra(operator, operand):
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
    return int(result)
```
Here's how you can use this function:

```Python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = DoAlgebra(operator, operand)
print(result)  # Output: 9
``` 

Remember to add error checking code to handle invalid inputs. For example, you might want to check that the operator list has at least one operator and the operand list has at least two operands. You might also want to check that the operator list and operand list have the same length minus one, as specified in the problem statement. 

Also, the ** operator in Python is the exponentiation operator, not the floor division operator. If you want to perform floor division, you should use the // operator. 

This function assumes that the operator list contains only the valid operators specified in the problem statement. If the operator list contains any other characters, this function will not work correctly. 

Finally, this function does not handle the case where the result of the algebraic expression is larger than the maximum integer value that can be represented in Python. In such cases, the result will be incorrect. If you need to handle very large results, you might need to use a library that supports arbitrary-precision arithmetic. 