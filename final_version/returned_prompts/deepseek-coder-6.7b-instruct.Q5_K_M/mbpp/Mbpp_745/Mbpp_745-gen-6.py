Here is the Python function for the problem:

```python
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        digits = [int(d) for d in str(num) if d != '0']
        if all(num % d == 0 for d in digits):
            result.append(num)
    return result
```

You can use this function by calling it with the desired range, like this:

```python
print(divisible_by_digits(1, 22))
```

This will output:

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

This function works by iterating over each number in the given range. It then converts the number to a string to get its digits, and uses a list comprehension to create a list of those digits. The function then checks if the number is divisible by every digit using the all() function combined with a generator expression. If the number is divisible by all of its digits, it is added to the result list. Finally, the function returns the result list.

This function assumes that the startnum and endnum are both nonnegative integers.
"""

def test_divisible_by_digits():
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(10,20)==[12, 14, 15, 16, 18, 20]
    assert divisible_by_digits(50,60)==[54, 60]
    assert divisible_by_digits(100,200)==[125, 150, 200]
    assert divisible_by_digits(1000,