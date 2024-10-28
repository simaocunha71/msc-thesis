```
def count_charac(s):
    return len(s)
```
The task is to create a function that counts the total number of characters in a given string. 

The provided unit test `assert count_charac("python programming")==18` suggests that the function should count all characters in the string, including spaces and punctuation. 

In this case, the solution is to use the built-in `len` function in Python, which returns the number of items in an object. When the object is a string, `len` returns the number of characters in the string.

So, the function `count_charac` takes a string `s` as input and returns the length of the string, which is the total number of characters. 

For example, `count_charac("python programming")` would return `18`, which is the total number of characters in the string "python programming". 