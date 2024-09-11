To solve this problem, you can follow these steps:

1. Define a function called index_minimum that takes in a list of tuples.
2. Initialize a variable called min_val to the first tuple in the list. This variable will store the tuple with the smallest second value.
3. Use a for loop to iterate through the list of tuples. For each tuple, compare the second value (index 1) to the second value of the current min_val tuple.
4. If the second value of the current tuple is smaller than the second value of min_val, update min_val to be the current tuple.
5. After the for loop has finished iterating through all the tuples, return the first value (index 0) of min_val, which will be the value from the tuple with the smallest second value.
6. Test the function with the provided example and assert that the output is correct.

Here is the code that implements these steps:

```python
def index_minimum(tuples):
    min_val = tuples[0]
    for t in tuples:
        if t[1] < min_val[1]:
            min_val = t
    return min_val[0]

assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
```

This code defines the index_minimum function and tests it with the provided example. The function correctly returns 'Varsha' as the first value of the tuple with the smallest second value.

"""

def index_minimum(tuples):
    min_val = tuples[0]
    for t in tuples:
        if t[1] < min_val[1]:
            min_val = t
    return min_val[0]

assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'

"""

To solve this problem, you can follow these steps:

1. Define a function called index_minimum that takes in a list of tuples.
2. Initialize a variable called min_val to