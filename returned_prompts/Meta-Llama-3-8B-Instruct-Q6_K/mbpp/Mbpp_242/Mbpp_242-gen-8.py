```
def count_charac(s):
    return len(s)
```


Explanation:
The task is to write a function that counts the total number of characters in a given string. The function should take a string as an argument and return the total count of characters in that string.

The unit test provided is `assert count_charac("python programming")==18`, which helps to clarify the expected behavior of the function. The test checks if the function returns the correct count of characters in the given string.

The solution is to use the built-in `len()` function in Python, which returns the number of items in an object. In this case, we pass the string `s` to `len()` to get the total count of characters in the string. The function is defined as `count_charac(s) = len(s)`. This function will pass the provided unit test.