```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and num > 0:
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count
```



Explanation:
This function iterates over each number in the input array. For each number, it checks if the number is greater than 10 and greater than 0 (to ensure it's a positive number). If the number passes these conditions, it extracts the first and last digits of the number using string slicing and integer conversion. It then checks if both digits are odd (i.e., not divisible by 2) by using the modulus operator. If both digits are odd, it increments the count. Finally, the function returns the count of numbers that meet the conditions.  For example, for the input [15, -73, 14, -15], the function would return 1, because only 15 meets the conditions. Similarly, for the input [33, -2, -3, 45, 21, 109], the function would return 2, because both 33 and 109 meet the conditions.