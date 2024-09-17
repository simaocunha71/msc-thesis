```
def count_list(list_of_lists):
    return len(list_of_lists)
``` 
This function takes a list of lists as an argument and returns the number of lists in that list. The unit test provided ensures that the function works correctly. For example, if the input is `[[1, 3], [5, 7], [9, 11], [13, 15, 17]]`, the function should return `4`, which is the number of lists in the input. 

The function uses the built-in `len` function in Python, which returns the number of items in an object. When the object is a list, `len` returns the number of elements in the list. Therefore, in this case, `len(list_of_lists)` returns the number of lists in the input. 