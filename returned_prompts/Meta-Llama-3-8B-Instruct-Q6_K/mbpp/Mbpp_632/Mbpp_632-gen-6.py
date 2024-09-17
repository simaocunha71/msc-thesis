You can use list comprehension to create a new list where all zeroes are moved to the end. Here is the python function:

```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```
This function works by creating two lists: one for all elements that are not zero, and one for all elements that are zero. It then combines these two lists, with the non-zero elements first. This effectively moves all zeroes to the end of the list. 

You can use this function as follows:

```
print(move_zero([1,0,2,0,3,4]))  # Output: [1,2,3,4,0,0]
```
This will move all zeroes to the end of the list. 

The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that this function is working correctly.  It checks that the output of the function is equal to the expected output. If the output is not equal to the expected output, the function is not working correctly.  In this case, the function is working correctly.  



Another way to solve this problem is by two pointers approach. Here is the python function:

```
def move_zero(lst):
    non_zero = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero], lst[i] = lst[i], lst[non_zero]
            non_zero += 1
    return lst
```
This function works by iterating over the list and swapping each non-zero element with the element at the `non_zero` index. The `non_zero` index is incremented each time a non-zero element is found. This effectively moves all zeroes to the end of the list. 

You can use this function as follows:

```
print(move_zero([1,0,2,0,3,4]))  # Output: [1,2,3,4,0,0]
```
This will also move all zeroes to the end of the list.  



The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that this function is working correctly.  It checks that the output of the function is equal to