```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```


Explanation:
The function moves all zeroes to the end of the given list. It does this by using list comprehension to create two lists: one with all non-zero elements and one with all zero elements. It then concatenates these two lists together, effectively moving all zeroes to the end of the original list.

The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` helps to clarify the expected output of the function. The expected output is the original list with all zeroes moved to the end. This test ensures that the function is working correctly. 





