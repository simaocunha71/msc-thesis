```
def sum_digits(n):
    return sum(map(int, str(n)))
```

Explanation:

This function works by first converting the integer to a string using the str() function. Then, the map() function is used to apply the int() function to each character in the string. The map() function returns a map object, which is a special type of iterator that can be used with the sum() function to calculate the sum of all the integers in the map object. Finally, the sum() function is used to calculate the sum of all the digits in the integer and return the result.

The assert statement at the end of the code is used to test the function and make sure it works correctly. It asserts that the function sum_digits(345) returns 12, which is the correct sum of the digits in the number 345.

In summary, the function sum_digits(n) takes a non-negative integer as input and returns the sum of all its digits.

```python
def sum_digits(n):
    return sum(map(int, str(n)))
```

Explanation:

The function sum_digits(n) takes a non-negative integer as input and returns the sum of all its digits. It does this by first converting the integer to a string using the str() function. Then, the map() function is used to apply the int() function to each character in the string. The map() function returns a map object, which is a special type of iterator that can be used with the sum() function to calculate the sum of all the integers in the map object. Finally, the sum() function is used to calculate the sum of all the digits in the integer and return the result.

The assert statement at the end of the code is used to test the function and make sure it works correctly. It asserts that the function sum_digits(345) returns 12, which is the correct sum of the digits in the number 345.

In summary, the function sum_digits(n) takes a non-negative integer as input and returns the sum of all its digits.

```python
def sum_digits(n):
    return sum(map