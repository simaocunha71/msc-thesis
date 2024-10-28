```
def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum + 1):
        if all(int(digit) in str(i) and i % int(digit) == 0 for digit in str(i)):
            result.append(i)
    return result
```



This function works by iterating over the range from `startnum` to `endnum` (inclusive). For each number `i` in this range, it checks if every digit in `i` is a divisor of `i`. If this is the case, it adds `i` to the result list. The `all` function is used to check if a condition is true for all elements in an iterable. The condition is that the digit is in the string representation of `i` and that `i` is divisible by the digit. The `int(digit)` is used to convert the digit from a string to an integer. The `str(i)` is used to convert the number `i` to a string, so that we can iterate over its digits. The `i % int(digit) == 0` is used to check if `i` is divisible by the digit. If `i` is divisible by every digit it contains, it is added to the result list. The function finally returns the result list. 





The unit test `assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` shows that the function should return all numbers within the given range that are divisible by every digit they contain. The expected output is a list of numbers. The function should return the correct list of numbers for the given range. 





This function has a time complexity of O(n*m) where n is the range and m is the maximum number of digits in a number in the range. This is because for each number in the range, we are iterating over its digits. The space complexity is O(n) because we are storing the result in a list. 





The function can be optimized by only checking the digits up to 9, because numbers with digits greater than 9 will not be divisible by every digit they contain. This would reduce the time complexity to O(n) because we would only be iterating over the digits up to 9 for each number in the range. The space complexity