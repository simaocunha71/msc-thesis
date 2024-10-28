```
def substract_elements(t1, t2):
    return tuple(i - j for i, j in zip(t1, t2))
```


The problem is asking you to create a function that takes two tuples as input and returns a new tuple where each element is the result of subtracting the corresponding element from the second tuple from the element in the first tuple.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` helps to clarify the problem by providing an example of the expected output.

The solution uses the `zip` function to pair up the elements from the two tuples, and then uses a generator expression to subtract the elements of the second tuple from the elements of the first tuple. The result is a new tuple that is returned by the function.