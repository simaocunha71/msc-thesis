```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```
The function `move_zero` takes a list `lst` as input and returns a new list where all zeroes are moved to the end. It uses list comprehension to create two lists: one with all non-zero elements and one with all zero elements. It then concatenates these two lists to produce the result. The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that the function works correctly.