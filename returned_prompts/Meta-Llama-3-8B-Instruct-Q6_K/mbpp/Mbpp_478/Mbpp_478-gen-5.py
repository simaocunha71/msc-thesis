```
def remove_lowercase(s):
    return ''.join(c for c in s if not c.islower())
```
This function uses a generator expression to iterate over each character `c` in the input string `s`. The `islower()` method is used to check if a character is lowercase, and if it is, the character is skipped. The `join()` method is then used to concatenate the remaining characters into a new string, which is returned by the function. 

For example, if the input string is "PYTHon", the function will return "PYTH", as it removes the lowercase "o" from the string. 

The unit test `assert remove_lowercase("PYTHon")==('PYTH')` ensures that this function works correctly.  It checks that the output of the function is "PYTH", which is the string resulting from removing the lowercase "o" from the input string "PYTHon".  The parentheses around the expected output are used to ensure that the comparison is made character-by-character, rather than as a whole string.  This is necessary because the problem statement asks for the function to return a string, but the unit test is comparing the output to a string that has been wrapped in parentheses.  Without the parentheses, the comparison would be made as a whole string, and the test would fail.  With the parentheses, the comparison is made character-by-character, and the test passes. 