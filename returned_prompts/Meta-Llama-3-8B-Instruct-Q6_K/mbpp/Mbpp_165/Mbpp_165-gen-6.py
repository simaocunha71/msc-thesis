You can solve this problem as follows:

```python
def count_char_position(s):
    return sum(1 for c in s if c.lower() == chr(ord('a') + ord(c.lower()) - ord('a')))
```



In this problem, you need to write a function that counts the number of characters in a given string that occur at the same position in the string as in the English alphabet (case insensitive).

For example, if the input string is "xbcefg", the output should be 2 because 'c' and 'e' are the characters that occur at the same position in the string as in the English alphabet.

The unit test `assert count_char_position("xbcefg") == 2` helps to clarify this problem by providing a specific example.

The solution to this problem is a function named `count_char_position` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string. For each character, it checks if the lowercase version of the character is equal to the lowercase version of the character at the same position in the English alphabet (case insensitive). If the characters are equal, it counts it as 1. The `sum` function is then used to add up all the counts.

This function returns the total count of characters that occur at the same position in the string as in the English alphabet (case insensitive). For example, if the input string is "xbcefg", it returns 2 because 'c' and 'e' are the characters that occur at the same position in the string as in the English alphabet.