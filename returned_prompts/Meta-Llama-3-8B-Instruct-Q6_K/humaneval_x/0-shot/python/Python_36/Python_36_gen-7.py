```
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
```


The provided code defines a function `fizz_buzz(n: int)` that calculates the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

The function iterates over the range `1` to `n-1` (inclusive) and checks if each integer is divisible by either 11 or 13. If an integer is divisible by one of these numbers, it is converted to a string and the count of the digit 7 is incremented. The total count is then returned.

The provided unit tests demonstrate the correctness of the function. For example, `fizz_buzz(50)` returns 0 because there are no integers less than 50 that are divisible by 11 or 13, and therefore, the digit 7 does not appear in any of these integers. Similarly, `fizz_buzz(78)` returns 2 because the integers 77 and 73 are divisible by 11 or 13 and contain the digit 7. Finally, `fizz_buzz(79)` returns 3 because the integers 77, 73, and 79 are divisible by 11 or 13 and contain the digit 7.