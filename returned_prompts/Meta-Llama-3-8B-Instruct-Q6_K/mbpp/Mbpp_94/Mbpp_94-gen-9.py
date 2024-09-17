```
def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]
```
The function `index_minimum` takes a list of tuples as input and returns the first element of the tuple with the smallest second element. The `min` function is used with a `key` function that specifies that the second element of each tuple should be used for comparison. The `[0]` at the end is used to extract the first element of the resulting tuple. 

For example, given the list `[( 'Rash', 143), ( 'Manjeet', 200), ( 'Varsha', 100)]`, the function would return `'Varsha'` because it is the first element of the tuple with the smallest second element, which is `( 'Varsha', 100)`. This is confirmed by the unit test `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'`. 