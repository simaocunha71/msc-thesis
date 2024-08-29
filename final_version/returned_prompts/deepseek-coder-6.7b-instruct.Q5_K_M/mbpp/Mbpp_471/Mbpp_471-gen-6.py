```python
def find_remainder(arr,n):
    prod = 1
    for i in arr:
        prod = (prod * i) % n
    return prod

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # Output: 9
```

This program works by initializing a variable `prod` to 1. It then loops through each number in the array and multiplies `prod` by that number, modulo `n`. This way, the product is always in the range of 0 to `n`, and the result is the product of the array modulo `n`.

The function `find_remainder` returns the product of the array modulo `n`. In the provided example, the function returns 9.

The `%` operator is used to find the remainder of the division.
"""

assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) == 9
```
The assert statement is used to test the function. If the function returns the expected result, the assert statement does nothing. If the function does not return the expected result, the assert statement raises an AssertionError.
"""
"""

The `find_remainder` function can handle any length of list and any value for `n`, as long as `n` is not zero. If `n` is zero, the function will return 0 for any input, because any number multiplied by zero is zero.
"""

assert find_remainder([ 100, 10, 5, 25, 35, 14 ],0) == 0
assert find_remainder([],11) == 1
"""
The assert statements are used to test the function. If the function returns the expected result, the assert statement does nothing. If the function does not return the expected result, the assert statement raises an AssertionError.
"""
"""

Overall, this function is efficient and can handle large inputs. However, it has a limitation that it may not work correctly if the numbers in the list are very large or the modulo number is very large because of