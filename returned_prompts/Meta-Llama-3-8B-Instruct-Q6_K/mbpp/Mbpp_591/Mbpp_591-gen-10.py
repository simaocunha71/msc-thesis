```
def swap_List(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
```
The function takes a list as input and checks if the list has more than one element. If it does, it swaps the first and last elements using tuple unpacking. Finally, it returns the modified list. The unit test `assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]` ensures that the function works correctly. 

The function will not work correctly if the input list has one or zero elements, but this is not a problem because the problem statement does not specify what to do in these cases. If you want to handle these cases, you can add additional checks and handle them as needed. For example, you could raise an exception if the input list has zero elements, or return the original list if it has one element. 

Here's an updated version of the function that handles these cases:
```
def swap_List(lst):
    if len(lst) < 2:
        if len(lst) == 0:
            raise ValueError("Input list is empty")
        elif len(lst) == 1:
            return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
```
This version of the function raises a `ValueError` if the input list is empty, and returns the original list if it has one element. It will still swap the first and last elements if the input list has more than one element. 