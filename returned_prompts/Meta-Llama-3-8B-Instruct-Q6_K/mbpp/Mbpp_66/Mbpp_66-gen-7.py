```
def pos_count(lst):
    return len([i for i in lst if i > 0])
```
This function uses a list comprehension to create a list of all positive numbers in the input list, and then returns the length of that list, which is the number of positive numbers. The unit test `assert pos_count([1,-2,3,-4]) == 2` ensures that the function works correctly. 

Here is the explanation of the code:
- `lst` is the input list
- `[i for i in lst if i > 0]` is a list comprehension that creates a new list with all elements `i` from `lst` where `i > 0`
- `len([i for i in lst if i > 0])` returns the length of this new list, which is the number of positive numbers in `lst`
- `return` statement returns the length of the list. 