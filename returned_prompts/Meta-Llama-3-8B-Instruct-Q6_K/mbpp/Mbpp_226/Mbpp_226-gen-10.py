```
def odd_values_string(s):
    return ''.join(s[i] for i in range(0, len(s), 2))
```



The problem is asking to create a function that takes a string as an input and returns a new string where all characters at odd index positions are removed.

For example, if the input string is 'abcdef', the function should return 'ace' because 'a' is at index 0, 'c' is at index 2, and 'e' is at index 4, all of which are even index positions.

Here is a Python function that solves this problem:

```
def odd_values_string(s):
    return ''.join(s[i] for i in range(0, len(s), 2))
```

This function uses a generator expression to iterate over the indices of the input string `s`. The `range` function is used to generate indices starting from 0 and incrementing by 2 each time, effectively skipping the odd index positions. The `join` method is then used to concatenate the characters at these even index positions into a new string. The `join` method takes an iterable of strings as its argument and concatenates them into a single string, with the strings separated by the string on which the method is called. In this case, the `join` method is called on an empty string, so the characters are simply concatenated without any separators.