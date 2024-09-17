```
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
```


This function uses a list comprehension to create a new list that includes only the elements of the original list that are even (i.e., where `i % 2 == 0`). The function then returns this new list. The unit test `assert remove_odd([1,2,3]) == [2]` confirms that this function works as expected. 

Note: This function does not modify the original list, but instead returns a new list that meets the specified criteria. If you want to modify the original list, you could use a for loop to iterate over the list and remove the odd numbers, but this would require more code and would not be a good fit for a list comprehension. 







