def split(string):
    return list(string)


# Created by: Nutta Sutthivech
# Date: 12/11/2018


# Test Case:
print(split("python"))  # should print: ['p', 'y', 't', 'h', 'o', 'n']
print(split("Hello World!"))  # should print: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

The function `split` accepts a string as an argument and returns a list of each character in the string.

The `list` function is used to convert the string into a list of characters.

In the test cases, the function is called with different strings and the expected outputs are provided.

The first test case `print(split("python"))` should print `['p', 'y', 't', 'h', 'o', 'n']` as the expected output.

The second test case `print(split("Hello World!"))` should print `['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']` as the expected output.