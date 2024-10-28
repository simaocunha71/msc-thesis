```
def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]
```


The function `index_minimum` takes a list of tuples as input and returns the first value of the tuple with the smallest second value. It uses the built-in `min` function with a custom key function to find the tuple with the smallest second value. The key function is a lambda function that takes a tuple and returns its second value. The `min` function then returns the tuple with the smallest second value, and the function returns the first value of this tuple.

The unit test `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'` ensures that the function works correctly. It checks that the function returns the first value of the tuple with the smallest second value, which is 'Varsha' in this case.