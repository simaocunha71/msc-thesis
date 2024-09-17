```
def div_list(list1, list2):
    return [i/j for i, j in zip(list1, list2)]
```


This function uses a list comprehension to iterate over the two input lists in parallel, using the zip function to pair up corresponding elements. It then divides each pair of elements and returns the results as a new list. The division is done using the '/' operator, which performs floating point division.

For example, if we call `div_list([4,5,6],[1, 2, 3])`, the function will return `[4.0, 2.5, 2.0]`, as expected.

Note that the function does not perform any error checking, so it will raise a ZeroDivisionError if any element in the second list is zero. If you want to handle this case, you could add a conditional statement to the list comprehension, like this:
```
def div_list(list1, list2):
    return [i/j if j != 0 else 0 for i, j in zip(list1, list2)]
```
This will replace any division by zero with a result of 0.0. You could also add a try-except block to catch the ZeroDivisionError and handle it in a more sophisticated way. For example:
```
def div_list(list1, list2):
    return [i/j if j != 0 else 0 for i, j in zip(list1, list2)]
```


This will replace any division by zero with a result of 0.0. You could also add a try-except block to catch the ZeroDivisionError and handle it in a more sophisticated way. For example:
```
def div_list(list1, list2):
    result = []
    for i, j in zip(list1, list2):
        try:
            result.append(i/j)
        except ZeroDivisionError:
            result.append(0)
    return result
```
This will append a result of 0 to the output list whenever a division by zero occurs. You could also choose to raise a custom exception, or to handle the error in some other way, depending on your specific requirements.