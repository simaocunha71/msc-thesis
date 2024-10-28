```
def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())
```


The task is to create a function that takes a string as input and returns a new string with all uppercase characters removed. 

The unit test provided suggests that the function should return 'cstyoravoitshos' when given the input 'cAstyoUrFavoRitETVshoWs'. 

To solve this problem, we can use Python's built-in string method `islower()` which returns `True` if a character is lowercase and `False` if it's uppercase. We can use a generator expression to iterate over each character in the input string, and then join these characters back together into a new string using the `join()` method. 

Here's the solution:

```
def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())
```


This function works by iterating over each character `c` in the input string `s`. If the character is lowercase (i.e., `c.islower()` returns `True`), it is included in the new string. If the character is uppercase, it is skipped. The resulting string is then returned. 

For example, when given the input 'cAstyoUrFavoRitETVshoWs', the function will return 'cstyoravoitshos', which is the desired output. 