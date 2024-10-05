You can use the following Python solution to solve this problem:

```python
def even_odd_count(n):
    even_count = 0
    odd_count = 0
    for digit in str(abs(n)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```

This function works by first converting the input number to a string and then iterating over each character (digit) in the string. For each digit, it checks whether the digit is even (by checking if the remainder of the digit divided by 2 is 0) and increments the corresponding count. Finally, it returns a tuple of the two counts. The abs function is used to handle negative numbers.

For example, if you call even_odd_count(-12), it will return (1, 1), which means there is one even digit (2) and one odd digit (1). If you call even_odd_count(123), it will return (1, 2), which means there is one even digit (3) and two odd digits (1, 3).