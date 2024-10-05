```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and num % 10 % 2 != 0 and str(num)[0] % 2 != 0:
            count += 1
    return count
```


Here's an explanation of the solution:
The function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that meet the specified conditions.

The conditions are:
1. The number is greater than 10.
2. The last digit of the number is odd (i.e., the remainder of the number divided by 2 is not 0).
3. The first digit of the number is odd.

To check these conditions, we iterate over the input array `nums`. For each number `num`, we check if it meets the conditions:
- `num > 10` checks if the number is greater than 10.
- `num % 10 % 2 != 0` checks if the last digit of the number is odd (because `num % 10` gives the last digit, and `num % 10 % 2` checks if it's odd).
- `str(num)[0] % 2 != 0` checks if the first digit of the number is odd (because `str(num)[0]` gives the first character of the string representation of the number, and `str(num)[0] % 2` checks if it's odd).

If a number meets all these conditions, we increment the `count` variable.

Finally, we return the `count` variable, which represents the number of elements in the array that meet the specified conditions.