```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and str(num)[0] in '13579' and str(num)[-1] in '13579':
            count += 1
    return count
```
This function iterates over each number in the input array. For each number, it checks if the number is greater than 10 and if the first and last digits of the number are odd. If both conditions are met, it increments a counter. Finally, it returns the count. The str(num)[0] expression gets the first character of the string representation of the number, and the str(num)[-1] expression gets the last character. The in '13579' checks if the character is one of the odd digits (1, 3, 5, 7, 9). If both conditions are true, it adds 1 to the count. At the end, it returns the count. This function works for the given examples and should work for any array of numbers.