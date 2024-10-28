```
def div_list(list1, list2):
    return [i/j for i, j in zip(list1, list2)]
``` 

The function takes two lists as input and returns a new list where each element is the result of dividing the corresponding elements from the input lists. The zip function is used to iterate over the two lists in parallel, and a list comprehension is used to create the new list. 

This function assumes that the input lists are of the same length, and that the second list is not empty. If the second list is empty, a ZeroDivisionError will be raised. 

The unit test provided ensures that the function behaves correctly for the given input. It checks that the function returns the correct result for the input lists [4,5,6] and [1, 2, 3]. 

Here is the unit test:
```
assert div_list([4,5,6],[1, 2, 3]) == [4.0,2.5,2.0]
``` 





The function can be further modified to handle cases where the second list is empty, by checking the length of the second list before performing the division. Here is an example of how you could do this:

```
def div_list(list1, list2):
    if len(list2) == 0:
        return []
    return [i/j for i, j in zip(list1, list2)]
```

This modified function will return an empty list if the second input list is empty, instead of raising a ZeroDivisionError.