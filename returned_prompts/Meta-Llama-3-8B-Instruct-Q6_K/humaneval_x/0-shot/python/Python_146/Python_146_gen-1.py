The problem can be solved by iterating over the array and checking each number to see if it satisfies the given conditions. Here is a Python function that does this:

```Python
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            if int(str(num)[0]) % 2 != 0 and int(str(num)[-1]) % 2 != 0:
                count += 1
    return count
```

This function works by iterating over each number in the input array. If the number is greater than 10, it converts the number to a string and checks the first and last characters (which represent the first and last digits of the number). If both of these digits are odd (i.e., not divisible by 2), it increments a count variable. Finally, the function returns the count of numbers that satisfy the conditions. 

For example, if you call `specialFilter([15, -73, 14, -15])`, the function will return 1, because only 15 satisfies the conditions. If you call `specialFilter([33, -2, -3, 45, 21, 109])`, the function will return 2, because both 33 and 109 satisfy the conditions. 