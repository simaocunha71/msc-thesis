def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]

# Test case
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))  # Output: 'Varsha'
```
This function takes a list of tuples as input and returns the first value of the tuple with the smallest second value. It uses the built-in `min` function with a `key` function to specify that it should find the tuple with the smallest second value. The `key` function is a lambda function that returns the second value of each tuple. The `min` function then returns the tuple with the smallest second value, and the function returns the first value of this tuple (using indexing).  



