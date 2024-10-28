```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```


The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` suggests that the function should move all zeroes to the end of the list. The provided solution uses list comprehension to achieve this. It first creates a list of non-zero elements and then adds a list of zero elements at the end. This ensures that all zeroes are moved to the end of the list.