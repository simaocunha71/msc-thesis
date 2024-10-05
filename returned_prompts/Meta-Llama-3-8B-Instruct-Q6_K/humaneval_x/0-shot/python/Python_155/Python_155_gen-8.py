
```
def even_odd_count(num):
    num = str(abs(num))  # convert to string and take absolute value
    even_count = 0
    odd_count = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
```
This function first converts the input number to a string and takes the absolute value to handle negative numbers. Then, it iterates over each digit in the string, checks if the digit is even or odd by using the modulus operator (`%`), and increments the corresponding count. Finally, it returns a tuple containing the counts of even and odd digits.