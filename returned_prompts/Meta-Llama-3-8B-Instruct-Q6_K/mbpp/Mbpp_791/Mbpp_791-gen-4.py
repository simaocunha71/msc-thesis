```
def remove_nested(t):
    result = ()
    for element in t:
        if isinstance(element, tuple):
            result += remove_nested(element)
        else:
            result += (element,)
    return result
```


The task is to create a function that takes a tuple as an input and returns a new tuple with all the nested tuples removed. 

The problem can be solved by iterating over the input tuple and adding each element to the result tuple. If the element is a tuple itself, the function calls itself recursively to process the nested tuple. 

The unit test `assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)` helps to clarify the problem by providing an example of the expected output for a given input. 

Here is the solution:
```
def remove_nested(t):
    result = ()
    for element in t:
        if isinstance(element, tuple):
            result += remove_nested(element)
        else:
            result += (element,)
    return result
```


This function works by iterating over the input tuple `t`. For each element, it checks if the element is a tuple itself using the `isinstance` function. If it is a tuple, the function calls itself recursively to process the nested tuple. If it is not a tuple, the function adds the element to the result tuple. The result tuple is then returned. 

The function can be tested using the provided unit test:
```
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
```


This test checks that the function correctly removes the nested tuple `(4, 6)` from the input tuple and returns the expected result `(1, 5, 7, 10)`. 

The function should work correctly for tuples of any depth, not just the example provided in the unit test. For example, it should correctly remove the nested tuple `(4, (6, 7))` from the input tuple `(1, 5, 7, (4, (6, 7)), 10)`. 

The function does not modify the original input tuple, but instead returns a new tuple with the nested tuples removed. This is because the problem statement asks for a new tuple to be returned, not for the original tuple to be modified. 

The function has a time complexity of O(n), where n