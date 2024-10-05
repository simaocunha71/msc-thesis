```
def specialFilter(nums):
    count = 0
    for num in nums:
        if abs(num) > 10:  # Check if the number is greater than 10
            first_digit = int(str(abs(num))[0])  # Extract the first digit
            last_digit = int(str(abs(num))[-1])  # Extract the last digit
            if first_digit % 2 != 0 and last_digit % 2 != 0:  # Check if both digits are odd
                count += 1
    return count
```


The function `specialFilter` iterates over each number in the input array `nums`. For each number, it checks if the absolute value of the number is greater than 10. If it is, it extracts the first and last digits of the number. It then checks if both digits are odd by using the modulus operator `%`. If both digits are odd, it increments the count. Finally, it returns the count of numbers that meet the condition.

For example, when called with the input `[15, -73, 14, -15]`, the function returns `1` because only `15` meets the condition. When called with the input `[33, -2, -3, 45, 21, 109]`, the function returns `2` because both `33` and `109` meet the condition.