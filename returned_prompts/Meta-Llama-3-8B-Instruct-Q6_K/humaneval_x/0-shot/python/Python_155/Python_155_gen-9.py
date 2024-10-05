```
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
```


This function works by first converting the input number to a string, so we can iterate over each digit. We then use the modulus operator to check if each digit is even or odd. If the remainder is 0, the digit is even, otherwise it's odd. We keep a count of each, and finally return the counts as a tuple. The `abs` function is used to handle negative numbers, which would otherwise be treated as having all odd digits.