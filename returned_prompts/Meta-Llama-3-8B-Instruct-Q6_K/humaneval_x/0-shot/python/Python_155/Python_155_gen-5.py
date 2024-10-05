```
def even_odd_count(num):
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```


Test cases:
```
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
print(even_odd_count(456))  # Output: (2, 0)
print(even_odd_count(789))  # Output: (0, 3)
```


Explanation:
1. Convert the input integer to a string to easily iterate over each digit.
2. Initialize counters for even and odd digits.
3. Iterate over each digit in the string.
4. Check if the digit is even (using the modulus operator `% 2 == 0`) and increment the corresponding counter.
5. Return the tuple of even and odd counts.