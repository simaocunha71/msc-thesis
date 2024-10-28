To solve this kata, you should:

- Check if all of the input values are integers. If any of them are not, return False. You can use the `isinstance()` function to check this.
- Check if the sum of two of the numbers is equal to the third number. You can use the `sum()` function to calculate the sum of two numbers. If the sum is equal to the third number, return True. Otherwise, return False.

Here's a step-by-step explanation of the solution:

1. Start by defining the `any_int()` function and passing in three parameters: `x`, `y`, and `z`.
2. Check if all of the input values are integers by using the `isinstance()` function. If any of them are not integers, return False.
3. Calculate the sum of two of the numbers using the `sum()` function. For example, if `x` is 3 and `y` is 2, the sum will be 5.
4. Check if the sum is equal to the third number. If the sum is equal to the third number, return True. Otherwise, return False.
5. Return the result of the check.

Here's an example implementation of the solution:

```python
def any_int(x, y, z):
    # Check if all of the input values are integers
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    
    # Calculate the sum of two of the numbers
    sum_of_two = sum([x, y])
    
    # Check if the sum is equal to the third number
    if sum_of_two == z:
        return True
    else:
        return False
```

You can use this function to test different scenarios. For example, if you call `any_int(5, 2, 7)`, it will return True because the sum of 5 and 2 is equal to 7, and all of the numbers are integers. However, if you call `any_int(3, 2, 2)`, it will return False because the sum of 3 and 2 is not equal to 2, even though all of the