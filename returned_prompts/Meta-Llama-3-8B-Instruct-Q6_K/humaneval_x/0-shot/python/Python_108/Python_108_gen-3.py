```
def count_nums(arr):
    count = 0
    for num in arr:
        if num >= 0:
            if sum(int(digit) for digit in str(num)) > 0:
                count += 1
        else:
            if sum(int(digit) if digit != '-' else 0 for digit in str(abs(num))) > 0:
                count += 1
    return count
```


The function `count_nums` takes an array of integers as input and returns the number of elements in the array whose sum of digits is greater than 0. It iterates over each number in the array. If the number is non-negative, it calculates the sum of its digits and checks if it's greater than 0. If it is, it increments the count. If the number is negative, it calculates the sum of the digits of its absolute value, excluding the negative sign, and checks if the sum is greater than 0. If it is, it increments the count. Finally, it returns the count.