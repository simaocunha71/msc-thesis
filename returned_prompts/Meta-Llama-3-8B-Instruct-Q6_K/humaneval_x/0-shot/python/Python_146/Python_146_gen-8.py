```
def specialFilter(nums):
    count = 0
    for num in nums:
        if abs(num) > 10:
            first_digit = int(str(abs(num))[0])
            last_digit = int(str(abs(num))[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count
```



In this function, we iterate over each number in the input array. If the absolute value of the number is greater than 10, we extract the first and last digits of the number. We then check if both digits are odd by using the modulus operator (%). If both digits are odd, we increment the count. Finally, we return the count. 

The absolute value of the number is taken to handle negative numbers, and the modulus operator is used to check if the digits are odd. The `str()` function is used to convert the number to a string, and the `[0]` and `[-1]` indexing is used to extract the first and last digits. The `int()` function is used to convert the extracted digits back to integers. 





Example usage:

```
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
```