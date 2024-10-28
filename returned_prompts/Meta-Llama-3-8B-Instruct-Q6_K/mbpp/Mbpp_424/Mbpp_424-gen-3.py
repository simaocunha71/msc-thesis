```
def extract_rear(t):
    return [s[-1] for s in t]
```


The provided unit test `assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']` helps to understand the problem better. It suggests that the function should return a list of characters, each being the last character of a string in the input tuple. 

The problem can be solved by using a list comprehension in Python. The function `extract_rear` iterates over each string `s` in the input tuple `t`, and for each string, it extracts the last character `s[-1]` and adds it to the output list. The final output is a list of last characters of all strings in the input tuple. 

For example, `extract_rear(('Mers', 'for', 'Vers') )` will return `['s', 'r', 's']`, which matches the expected output in the unit test. 