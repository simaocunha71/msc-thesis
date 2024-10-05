
Here's a solution for you:

```python
def change_base(x: int, base: int):
    # Create a mapping of the base's digits to their ASCII values
    digit_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    result = ''
    while x > 0:
        # Calculate the remainder when dividing by the base
        remainder = x % base
        # Convert the remainder to a character using the digit_map
        remainder_char = digit_map[remainder]
        # Append the character to the result string
        result = remainder_char + result
        # Divide x by the base
        x = x // base
    return result
```

You can use the function like this:

```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

The function takes in two arguments: `x` (the number to be converted) and `base` (the base to convert the number to). It starts by creating a mapping of the base's digits to their ASCII values. Then, it enters a while loop where it calculates the remainder when dividing `x` by the base, converts the remainder to a character using the `digit_map`, and appends the character to the result string. After that, it divides `x` by the base and repeats the process until `x` becomes 0. Finally, it returns the result string, which is the converted number in the specified base.

The provided test cases demonstrate the usage of the function and the expected output.

I hope this helps! Let me know if you have any more questions.

```python

```

```python
def change_base(x: int, base: int):
    digit_map = {0: '