```
def flip_case(string: str) -> str:
    return ''.join([c.swapcase() for c in string])
```

In this solution, we use a list comprehension to iterate over each character `c` in the input string. For each character, we use the `swapcase()` method to flip its case (i.e., lowercase to uppercase or vice versa), and then join all these characters together into a new string using the `join()` method. This effectively flips the case of all characters in the input string.

For example, if we call `flip_case('Hello')`, the output would be `'hELLO'`. This is because the first character 'H' is uppercase and gets flipped to lowercase 'h', while the remaining characters 'e', 'l', 'l', 'o' are lowercase and get flipped to uppercase 'E', 'L', 'L', 'O'. The resulting string is `'hELLO'`.