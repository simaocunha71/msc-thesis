```
def even_odd_count(num):
    even = 0
    odd = 0
    num = abs(num)
    while num:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even, odd
```


The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits in the integer. The function works by first converting the input integer to its absolute value (in case it's negative). Then it enters a loop that continues until all digits of the integer have been processed. In each iteration of the loop, the function gets the last digit of the integer using the modulus operator (`%`), and checks whether it's even or odd by using the modulus operator again. If the digit is even, it increments the `even` counter; otherwise, it increments the `odd` counter. Finally, it removes the last digit from the integer by performing integer division by 10 (`//`). The function returns a tuple containing the `even` and `odd` counters as its result.