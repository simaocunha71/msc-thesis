```
def move_zero(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]
```
This function uses list comprehension to create two lists: one for non-zero elements and one for zero elements. It then concatenates these two lists to produce the desired output. The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures the function works as expected.