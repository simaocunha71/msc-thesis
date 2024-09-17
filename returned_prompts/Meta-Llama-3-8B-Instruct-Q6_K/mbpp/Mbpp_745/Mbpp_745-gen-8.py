```
def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(n):
        for digit in str(n):
            if n % int(digit) != 0:
                return False
        return True

    result = []
    for num in range(startnum, endnum+1):
        if is_divisible_by_digits(num):
            result.append(num)
    return result
```


The function `divisible_by_digits` takes two parameters `startnum` and `endnum` representing the range of numbers. It checks each number within this range to see if every digit in the number is divisible by the number itself. This is done by the function `is_divisible_by_digits`. If a number is found to be divisible by all its digits, it is added to the result list. The function returns this list of numbers.

The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` ensures that the function works correctly for the given range of numbers. The expected output is a list of numbers that are divisible by all their digits within the given range. The function should return this list. 





