Here is the Python code to solve the problem:

```python
def left_rotate(n, d):
    return (n << d)|(n >> (32 - d))

# Testing the function
print(left_rotate(16, 2)) # Output: 64
```

In the above function, `n` is the number and `d` is the number of bits to rotate. `n << d` is the left rotation and `n >> (32 - d)` is the right rotation. The `|` operator is used to combine these two rotations.

Note: The `<<` and `>>` operators are bitwise shift operators. `n << d` means n is left shifted by d bits which is equivalent to multiplying n by 2^d. `n >> d` means n is right shifted by d bits which is equivalent to integer division of n by 2^d.

Also note that we are assuming that the number is 32 bit. If the number is 64 bit, we would need to modify the code accordingly by changing the 32 to 64.

Lastly, this code does not handle cases where d is greater than 32. If you want to handle such cases, you would need to add an if statement to check if d is greater than 32 and if it is, then reset d to d % 32.

