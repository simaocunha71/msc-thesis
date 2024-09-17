```
def extract_rear(t):
    return [s[-1] for s in t]
```
The function `extract_rear` takes a tuple `t` as input and returns a list of characters. It uses a list comprehension to iterate over each string `s` in the tuple, and for each string, it extracts the last character using indexing (`s[-1]`). The resulting list of characters is then returned. The unit test `assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']` ensures that the function works correctly. 
Note: The problem statement is not clear about the return type of the function, but based on the unit test, it seems that the function should return a list of characters. If the problem statement is changed to return a list of strings, the function would be modified to return `['' for s in t]` instead. 