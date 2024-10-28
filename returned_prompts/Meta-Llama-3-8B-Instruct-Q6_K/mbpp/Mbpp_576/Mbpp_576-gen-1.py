The problem is asking to write a function that checks if a given list is a sublist of another list. A sublist is a contiguous portion of the main list.

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` suggests that a sublist must be a contiguous portion of the main list and not a random subset.

Here's a Python function that solves the problem:

```
def is_Sub_Array(main_list, sub_list):
    for i in range(len(main_list)):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False
```

This function iterates over the main list and checks if the sublist is present at any position in the main list. If it finds the sublist, it returns True. If it doesn't find the sublist after checking all positions, it returns False. 

Note that this function is case-sensitive and considers the order of elements. For example, [1, 2] is not a sublist of [2, 1]. 

Also, this function considers the sublist to be a contiguous portion of the main list. For example, [1, 2] is not a sublist of [1, 4, 3, 5] because it is not a contiguous portion of the main list. 

This function works correctly with the given unit test. It returns False for the test case `assert is_Sub_Array([1,4,3,5],[1,2]) == False` because [1, 2] is not a sublist of [1, 4, 3, 5].  It also returns False for the test case `assert is_Sub_Array([1,4,3,5],[1,4,3,5]) == True` because [1, 4, 3, 5] is a sublist of [1, 4, 3, 5].  It returns False for the test case `assert is_Sub_Array([1,2,3,4,5],[1,2]) == True` because [1, 2] is a sublist of [1, 2, 3, 4, 5].  It returns False for the test case `assert is_Sub_Array([1,2,3,4],[1,3,4]) == True` because [1, 3, 4] is a sublist of [1, 2, 3, 4].  It