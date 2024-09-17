```
def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]
```


This function uses the built-in `min` function with a `key` argument to find the tuple with the smallest second value. The `key` argument is a function that takes a tuple and returns its second value. The `min` function then returns the tuple with the smallest second value, and we use indexing to return the first value of that tuple. 

The unit test `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'` confirms that the function is working correctly. It checks that the function returns 'Varsha', which is the first value of the tuple with the smallest second value (100). 





