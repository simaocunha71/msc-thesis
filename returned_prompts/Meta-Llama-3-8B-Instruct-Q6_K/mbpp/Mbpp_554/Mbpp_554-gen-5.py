```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```
This function uses a list comprehension to iterate over the input list and includes only the elements that are odd (i.e., the remainder when divided by 2 is not 0). The result is a new list containing only the odd numbers from the original list. 

The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` ensures that the function works correctly. 

For example, if you call `Split([1,2,3,4,5,6])`, the function will return `[1,3,5]`, which are the odd numbers from the original list. 