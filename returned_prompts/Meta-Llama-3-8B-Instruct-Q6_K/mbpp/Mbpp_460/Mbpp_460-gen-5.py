```
def Extract(list_of_lists):
    return [i[0] for i in list_of_lists]
```


Explanation:
The problem is asking to write a function that takes a list of lists as input and returns a new list containing the first element of each sublist. 

The given unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` helps in understanding the problem better. 

The solution uses list comprehension to iterate over each sublist in the input list of lists and extract the first element. The result is a new list containing these first elements. 

The function is defined as `Extract(list_of_lists)` and it returns a new list using the list comprehension `[i[0] for i in list_of_lists]`. This list comprehension iterates over each sublist `i` in `list_of_lists` and extracts the first element `i[0]`. The resulting list of first elements is returned by the function. 

This function can be used to solve the problem as stated, and it passes the given unit test. 







