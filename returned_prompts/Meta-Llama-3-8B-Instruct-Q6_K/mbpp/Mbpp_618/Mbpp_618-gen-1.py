```
def div_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    return [i / j for i, j in zip(list1, list2)]
```


This function takes two lists as input and returns a new list where each element is the result of the division of the corresponding elements in the input lists. It first checks if the lists are of the same length, and if not, it raises a ValueError. Then it uses a list comprehension with the zip function to iterate over the pairs of elements from the input lists, dividing each pair and returning the result as a new list. The result is a list of floats, which is why the division operation is used instead of integer division. 

For example, if we call the function with the lists [4,5,6] and [1, 2, 3], it will return [4.0, 2.5, 2.0]. 

The unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` ensures that the function behaves as expected. 

Note that this function does not handle division by zero. If the input lists contain zeros and the function is called with these lists, it will raise a ZeroDivisionError. If you want to handle this case, you can add a check for zeros in the input lists and return a special value (like None or a custom error message) instead of raising an exception. 