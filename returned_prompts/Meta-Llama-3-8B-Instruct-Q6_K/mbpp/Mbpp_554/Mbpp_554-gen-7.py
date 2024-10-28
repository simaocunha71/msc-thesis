```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```
This function uses a list comprehension to create a new list that includes only the elements from the original list that meet the condition `i % 2 != 0`, which is true for odd numbers. The resulting list is then returned. The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` ensures that the function works correctly.