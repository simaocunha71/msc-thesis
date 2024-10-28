```
def count_char_position(s):
    count = 0
    for i, char in enumerate(s):
        if char.lower() == chr(ord('a') + i):
            count += 1
    return count
```


Here is the explanation:

The problem asks to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).

The given unit test `assert count_char_position("xbcefg") == 2` helps to understand the problem better. It means that in the string "xbcefg", the characters 'c' and 'e' occur at the same position as in the English alphabet (case insensitive).

The solution uses the `enumerate` function to iterate over the string along with their indices. Then, for each character, it checks if the character (converted to lowercase) is equal to the character at the same position in the English alphabet (case insensitive). If it is, it increments the count.

Here is the Python code for the solution:

```
def count_char_position(s):
    count = 0
    for i, char in enumerate(s):
        if char.lower() == chr(ord('a') + i):
            count += 1
    return count
```

This function takes a string `s` as input and returns the count of characters that occur at the same position as in the English alphabet (case insensitive). The `ord` function is used to get the ASCII value of 'a', and `chr` is used to convert the ASCII value back to the character. The `lower` method is used to make the comparison case insensitive. The `enumerate` function is used to iterate over the string along with their indices. The `if` statement checks if the character at the current position is equal to the character at the same position in the English alphabet, and if it is, the count is incremented. Finally, the function returns the count.