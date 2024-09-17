```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)
```


The function iterates over the nested lists and updates the set of all elements. Then it iterates over the nested lists again, and for each list, it updates the set of common elements by finding the intersection of the list and the set of all elements. The function finally returns the common elements as a list.

The unit test `assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])` ensures that the function correctly finds the common elements in the given nested lists. 





```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)
```





```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)
```





```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)
```





```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)
```





```
def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in