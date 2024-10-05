```
def fizz_buzz(n: int):
    count = 0
    for i in range(11, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
```
This function iterates over all integers less than `n` that are divisible by 11 or 13, converts each integer to a string, and counts the number of occurrences of the digit 7 in each string. The total count is returned. The function uses the modulo operator `%` to check for divisibility, and the `count` method of a string to count the occurrences of a digit.