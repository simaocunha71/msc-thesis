```
def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]
```


Explanation:
The function takes a list of tuples as input and returns the first value of the tuple with the smallest second value.

The `min` function is used with a `key` function that extracts the second value of each tuple. This returns the tuple with the smallest second value.

The `[0]` at the end is used to extract the first value of this tuple, which is the desired output.

This solution passes the given unit test:
```
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
```


This function will return 'Varsha' which is the first value of the tuple with the smallest second value (100).