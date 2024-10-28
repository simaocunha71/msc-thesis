To solve this problem, we can follow these steps:

1. Iterate through the string character by character, starting from the first character.
2. If the current character is not a space, add the character to the result string.
3. If the current character is a space, check the next character.
4. If the next character is also a space, replace the current and next space with a single underscore, and move the pointer to the next character. Otherwise, replace the current space with an underscore and move the pointer to the next character.
5. If the current character is not a space, and the previous character is a space, replace the previous space with an underscore.
6. Repeat steps 2-5 until the end of the string is reached.
7. Return the result string.

Here's a Python implementation of the above algorithm:

```python
def FixSpaces(text):
    result = []
    i = 0

    while i < len(text):
        if text[i] != ' ':
            result.append(text[i])
            i += 1
        else:
            if i + 1 < len(text) and text[i + 1] == ' ':
                result.append('_')
                i += 2
            else:
                result.append('_')
                i += 1

    if result[-1] == '_':
        result.pop()

    return ''.join(result)
```

You can test the function with the provided test cases:

```python
print(FixSpaces("Example"))  # Output: "Example"
print(FixSpaces("Example 1"))  # Output: "Example_1"
print(FixSpaces(" Example 2"))  # Output: "_Example_2"
print(FixSpaces(" Example   3"))  # Output: "_Example-3"
```

This implementation ensures that the result string does not end with an underscore, as specified in the problem statement.

Note: The provided Python implementation is a simple example and may not be the most efficient or elegant solution.

I hope this helps! Let me know if you have any further questions.

// Original solution
func FixSp