```
def count_charac(s):
    return len(s)
```


Explanation:
The problem is asking for a function that counts the total number of characters in a given string. 

The unit test provided, `assert count_charac("python programming")==18`, suggests that the function should return the total number of characters in the string. 

In Python, the built-in `len()` function is used to get the length of a string, which is the total number of characters. Therefore, the solution is to simply return the length of the input string. 

The function `count_charac(s)` can be implemented as follows: `def count_charac(s): return len(s)`. This function takes a string `s` as input and returns the total number of characters in the string. 

This solution passes the given unit test, as `count_charac("python programming")` returns `18`, which is the correct total number of characters in the string. 