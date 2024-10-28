```
def armstrong_number(n):
    num = str(n)
    length = len(num)
    sum = 0
    for digit in num:
        sum += int(digit) ** length
    return sum == n
```


This function works by first converting the input number into a string. Then it calculates the length of the string which is also the number of digits in the number. It then iterates over each digit in the string, converts it back into an integer, and raises it to the power of the length. It sums up all these values and checks if the sum is equal to the original number. If it is, the function returns True, meaning the number is an Armstrong number. Otherwise, it returns False. The unit test `assert armstrong_number(153)==True` ensures that the function correctly identifies the Armstrong number 153. 





