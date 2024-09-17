```
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(int(digit) in str(num) for digit in str(num)):
            result.append(num)
    return result
```





The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` suggests that the function should return all numbers within the range from `startnum` to `endnum` where every number is divisible by every digit it contains.

Here's the solution:

```python
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(int(digit) in str(num) for digit in str(num)):
            result.append(num)
    return result
```

This function iterates over the range from `startnum` to `endnum` (inclusive), and for each number, it checks if every digit in the number is present in the string representation of the number. If this condition is met, the number is added to the result list. Finally, the function returns the list of numbers that satisfy the condition.