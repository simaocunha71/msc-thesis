```
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
```


Explanation:
The problem is asking you to write a function that takes a list of tuples as an input and returns the first value of the tuple with the smallest second value.

The unit test provided helps to understand the problem better. It shows that the function should return 'Varsha' because 'Varsha' is the first value of the tuple with the smallest second value (100) in the list.

The solution to this problem can be achieved by using the built-in `min` function in Python. The `min` function can be used with a `key` argument, which is a function that takes a tuple and returns its second value. This will allow the `min` function to find the tuple with the smallest second value.

The `[0]` at the end is used to return the first value of the tuple, which is the desired output.

Here is the complete code:
```
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
```


This function will return the first value of the tuple with the smallest second value in the given list. For example, if the input list is `[('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]`, the function will return `'Varsha'`.