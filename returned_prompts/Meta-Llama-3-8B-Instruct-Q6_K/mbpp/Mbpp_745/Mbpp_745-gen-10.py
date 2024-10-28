```
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        is_divisible = True
        for digit in str(num):
            if num % int(digit) != 0:
                is_divisible = False
                break
        if is_divisible:
            result.append(num)
    return result
```
The function `divisible_by_digits` takes two parameters, `startnum` and `endnum`, and returns a list of numbers within the given range where every number is divisible by every digit it contains.

The function iterates over the range of numbers from `startnum` to `endnum` (inclusive). For each number, it checks if the number is divisible by every digit it contains. It does this by converting the number to a string and iterating over the digits. For each digit, it checks if the number is divisible by the integer value of the digit. If the number is not divisible by any digit, it sets the `is_divisible` flag to `False` and breaks out of the loop.

If the `is_divisible` flag is `True` after checking all digits, the function appends the number to the `result` list.

Finally, the function returns the `result` list.

The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` ensures that the function works correctly. It checks that the function returns the correct list of numbers within the range from 1 to 22 where every number is divisible by every digit it contains. The expected output is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]`, which includes all the numbers that meet the condition. If the function returns the correct list, the unit test passes; otherwise, it raises an AssertionError.