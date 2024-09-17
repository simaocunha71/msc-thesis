```
def is_lower(s):
    return s.lower()
```
Explanation: 
The problem is asking to create a function that converts a given string to lower case. The function should take a string as input and return the lower case version of the string. 

The unit test `assert is_lower("InValid") == "invalid"` suggests that the function should only convert the string to lower case. 

Python's built-in `lower()` function can be used to achieve this. It converts a string to lower case and returns the result. So, the solution is a simple function that calls `lower()` on the input string. 

This solution passes the given unit test. 

For example, if we call `is_lower("InValid")`, it will return `"invalid"`. 