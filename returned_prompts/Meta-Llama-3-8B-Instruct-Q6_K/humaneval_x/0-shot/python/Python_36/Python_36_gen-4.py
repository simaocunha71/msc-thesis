```
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
```


This function uses a for loop to iterate over all integers less than `n`. For each integer, it checks if it is divisible by 11 or 13 using the modulus operator `%`. If the integer is divisible by either 11 or 13, it converts the integer to a string and uses the `count` method to count the number of times the digit 7 appears in the string. It then adds this count to the total count. Finally, it returns the total count.