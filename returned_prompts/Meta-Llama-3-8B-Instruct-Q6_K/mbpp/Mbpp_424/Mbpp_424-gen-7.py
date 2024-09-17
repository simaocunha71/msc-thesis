```
def extract_rear(t):
    return [i[-1] for i in t]
```


Explanation:
The task is to write a function that takes a tuple of strings as input and returns a list containing the last character of each string in the tuple.

The unit test `assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']` helps to understand the problem better. It shows that the function should return a list of last characters of each string in the tuple.

The solution uses a list comprehension to iterate over the tuple and extract the last character of each string. The `i[-1]` expression is used to get the last character of each string, and the result is a list of these characters. The function returns this list. 

For example, when the input is `('Mers', 'for', 'Vers')`, the function returns `['s', 'r', 's']`.  This is because the last characters of the strings 'Mers', 'for', 'Vers' are 's', 'r', 's' respectively. 

The function works for any tuple of strings, not just the specific example given in the unit test. It is a general solution for the problem. 