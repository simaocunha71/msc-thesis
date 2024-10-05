```
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```


Output:
```
even_odd_count(-12) ==> (1, 1)
even_odd_count(123) ==> (1, 2)
```


Explanation:
- The function `even_odd_count` takes an integer as input and returns a tuple containing the number of even and odd digits respectively.
- We use a for loop to iterate over the digits of the input number. We convert the number to a string using the `str` function to easily iterate over the digits.
- We use the `abs` function to remove the sign of the number, as the problem statement does not specify whether to consider the sign of the number.
- We check each digit to see if it is even or odd by using the modulus operator `%`. If the remainder is 0, the digit is even, otherwise it is odd.
- We increment the corresponding count variable (even_count or odd_count) based on the parity of the digit.
- Finally, we return a tuple containing the even_count and odd_count.