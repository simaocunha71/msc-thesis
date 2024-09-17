```
def ascii_value(char):
    return ord(char)
```
The ord() function returns the ASCII value of a character. It is a built-in Python function that works with both lowercase and uppercase letters. For example, the ASCII value of 'A' is 65 and 'a' is 97. The function works with all characters, not just letters. For example, the ASCII value of '0' is 48 and '9' is 57. It also works with special characters like !, @, #, etc. 

The unit test `assert ascii_value('A')==65` ensures that the function works correctly for the uppercase letter 'A'. It checks if the function returns 65 for the input 'A', which is the ASCII value of 'A'. If the function is working correctly, this assertion should pass. 

The function can be tested with other characters as well. For example, `assert ascii_value('a')==97` should also pass, indicating that the function is working correctly for lowercase letters. Similarly, `assert ascii_value('0')==48` should pass, indicating that the function is working correctly for digits. 

This function can be used to find the ASCII value of any character in Python. It is a simple and efficient way to achieve this. 