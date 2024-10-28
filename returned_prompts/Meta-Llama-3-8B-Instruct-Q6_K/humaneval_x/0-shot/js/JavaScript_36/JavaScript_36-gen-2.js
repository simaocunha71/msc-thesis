Here is a Python solution for the problem:

```Python
def fizzBuzz(n):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            if '7' in str_i:
                count += 1
    return count
```

This function iterates over all numbers less than `n`, checks if the number is divisible by 11 or 13, converts the number to a string to check if it contains the digit 7, and increments the count if the number contains the digit 7. The function finally returns the count.