```
def specialFilter(nums):
    count = 0
    for num in nums:
        if abs(num) > 10 and str(abs(num))[0] % 2 != 0 and str(abs(num))[-1] % 2 != 0:
            count += 1
    return count
```


The function `specialFilter` iterates over each number in the input array `nums`. For each number, it checks if the absolute value of the number is greater than 10, and if the first and last digits of the number are odd. The first and last digits of a number are considered odd if the remainder of the number when divided by 2 is 1. The function uses the modulus operator `%` to check if the remainder of the number is 1.

The function returns the count of numbers in the array that satisfy the conditions.

For example, `specialFilter([15, -73, 14, -15])` returns 1 because the number 15 satisfies the conditions. `specialFilter([33, -2, -3, 45, 21, 109])` returns 2 because the numbers 33 and 109 satisfy the conditions.