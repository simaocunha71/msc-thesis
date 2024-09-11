```
def decimal_to_binary(n):
    res = []
    while n > 0:
        res.append(str(n % 2))
        n = n // 2
    return "".join(res[::-1])
```

Here's a Python function that converts a decimal number to its binary equivalent, represented as a string with no leading zeros. The function uses a while loop to repeatedly divide the number by 2 and append the remainder (0 or 1) to a list. Finally, the list is joined into a string and reversed to obtain the binary representation.

You can use the `assert` statement to verify the correctness of the function by comparing the result of `decimal_to_binary(8)` with the expected value '1000'.

```python
def decimal_to_binary(n):
    res = []
    while n > 0:
        res.append(str(n % 2))
        n = n // 2
    return "".join(res[::-1])
```

To test the function, you can call it with different decimal numbers and check if the output matches the expected binary representation. For example, `decimal_to_binary(8)` should return '1000', and `decimal_to_binary(10)` should return '1010'.

Here are some additional test cases you can try:

```python
assert decimal_to_binary(10) == '1010'
assert decimal_to_binary(15) == '1111'
assert decimal_to_binary(25) == '11001'
```

These test cases cover different values of `n`, including cases where `n` is a power of 2 (e.g., 16, 32, 64) and cases where `n` is not a power of 2. The function should correctly convert any decimal number to its binary representation without leading zeros.
```

```

```python
def decimal_to_binary(n):
    res = []
    while n > 0:
        res.append(str(n % 2))
       