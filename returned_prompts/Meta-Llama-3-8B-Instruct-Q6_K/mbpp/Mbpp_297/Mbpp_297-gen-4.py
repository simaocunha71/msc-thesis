```
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
```


The function works by iterating over each item in the list. If the item is a list itself, it recursively calls itself on that item and extends the result to the flat list. If the item is not a list, it simply appends it to the flat list.

The unit test `assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]` ensures that the function works correctly. It checks that the function returns a flat list of all the elements in the input list, including nested lists. 

This function will work for any depth of nested lists, not just for the example given in the unit test. It can handle lists with any number of levels of nesting. For example, it can handle a list like `[[[1, 2], 3], 4, [5, [6, 7]]]`. It will correctly flatten this list into a single list `[1, 2, 3, 4, 5, 6, 7]`. 

The time complexity of this function is O(n), where n is the total number of elements in the list. This is because the function visits each element in the list once. The space complexity is also O(n), because in the worst case, the function has to store all the elements in the list in the result. This is the case when the input list is a single element that is a list itself. For example, if the input is `[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]`, the function will have to store all 12 elements in the result. 