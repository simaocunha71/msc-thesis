```
def ascii_value(char):
    return ord(char)
```





Python has a built-in function called `ord()` that returns the ASCII value of a character. So, we can simply use this function to find the ASCII value of a character. The unit test `assert ascii_value('A')==65` ensures that the function returns the correct ASCII value for the character 'A'. 

Here is how you can use it:

```
print(ascii_value('A'))  # Output: 65
print(ascii_value('a'))  # Output: 97
```





The `ord()` function is case sensitive, so it will return different ASCII values for uppercase and lowercase letters. For example, 'A' and 'a' have different ASCII values. The ASCII value of 'A' is 65 and the ASCII value of 'a' is 97.