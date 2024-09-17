```
def add_pairwise(t):
    result = ()
    for i in range(1, len(t)):
        result += (t[i-1] + t[i],)
    return result
```


Explanation:
The problem is asking to create a function that takes a tuple as input and returns a new tuple where each element is the sum of the corresponding elements in the input tuple and its neighbor. 

For example, given the tuple (1, 5, 7, 8, 10), the function should return (6, 12, 15, 18), where each element is the sum of the corresponding element in the input tuple and its neighbor. 

The unit test `assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)` helps to clarify the problem by providing an example of the expected output.

Here is a Python function that solves the problem:
```
def add_pairwise(t):
    result = ()
    for i in range(1, len(t)):
        result += (t[i-1] + t[i],)
    return result
```
This function iterates over the input tuple starting from the second element (index 1) to the second last element. For each element, it adds the current element and its previous element to get the sum, and adds this sum to the result tuple. The function finally returns the result tuple.