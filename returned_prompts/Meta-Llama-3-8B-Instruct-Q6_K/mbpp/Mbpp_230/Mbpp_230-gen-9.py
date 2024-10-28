```
def replace_blank(s, c):
    return s.replace(" ", c)
```


Python's built-in string method `replace()` can be used to replace all occurrences of a substring with another substring. In this case, we are replacing all occurrences of a blank space (`" "`) with the given character (`c`). The `replace()` method returns a copy of the string where all occurrences of a substring have been replaced with another substring. It doesn't modify the original string. 

This function works as expected, as shown by the provided unit test:

```
assert replace_blank("hello people", '@') == "hello@people"
```


This test checks if the function `replace_blank` correctly replaces all blank spaces in the string "hello people" with the character '@', and the expected result is "hello@people". The `assert` statement will raise an `AssertionError` if the function returns anything other than "hello@people". Since the function works correctly, the test passes without raising an `AssertionError`. 