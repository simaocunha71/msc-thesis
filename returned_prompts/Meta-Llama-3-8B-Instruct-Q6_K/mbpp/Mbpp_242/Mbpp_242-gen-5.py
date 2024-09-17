```
def count_charac(s):
    return len(s)
```
The problem is asking to write a function that counts the total number of characters in a given string. 

The provided unit test `assert count_charac("python programming")==18` suggests that the function should return the total number of characters in the string, including spaces. 

We can achieve this by using the built-in `len` function in Python, which returns the number of items in an object. In this case, we can use `len` to count the number of characters in the string. 

Here's the solution:
```
def count_charac(s):
    return len(s)
```
This function takes a string `s` as input and returns the total number of characters in the string. The `len` function does the counting for us, so we don't need to write any additional code to do the counting. 

For example, if we call `count_charac("python programming")`, the function will return `18`, which is the total number of characters in the string, including the spaces. 