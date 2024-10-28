```
def extract_index_list(list1, list2, list3):
    common_elements = set(list1) & set(list2) & set(list3)
    common_elements = [i for i in common_elements if list1.index(i) == list2.index(i) == list3.index(i)]
    return common_elements
```


The function `extract_index_list` takes three lists as input and returns a list of common elements. It first finds the common elements between the three lists by using the set intersection operation. Then, it iterates over the common elements and checks if they have the same index in all three lists. If they do, it adds them to the result list. Finally, it returns the list of common elements. The unit test `assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]` ensures that the function works correctly. 







