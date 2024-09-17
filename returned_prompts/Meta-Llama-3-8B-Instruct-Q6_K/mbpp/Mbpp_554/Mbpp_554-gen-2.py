```
def Split(lst):
    return [i for i in lst if i % 2 != 0]
```
This function uses a list comprehension to iterate over the input list and only include the elements that are not divisible by 2 (i.e., the odd numbers). The result is a new list containing only the odd numbers from the original list. The unit test `assert Split([1,2,3,4,5,6]) == [1,3,5]` confirms that this function behaves as expected. 