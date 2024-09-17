```
def armstrong_number(n):
    temp = n
    sum = 0
    power = len(str(n))
    while n > 0:
        digit = n % 10
        sum += digit ** power
        n //= 10
    return sum == temp
```


The given number is considered as Armstrong number if the sum of the cubes of its digits is equal to the number itself. For example, the number 153 is an Armstrong number because 1*1*1 + 5*5*5 + 3*3*3 = 153.

In this function, we first calculate the number of digits in the given number. Then we calculate the sum of the cubes of the digits. Finally, we check if the sum is equal to the original number. If it is, then the number is an Armstrong number and we return True; otherwise, we return False. The unit test `assert armstrong_number(153)==True` ensures that the function is working correctly.