```
def extract_index_list(list1, list2, list3):
    common_index = set(list1) & set(list2) & set(list3)
    return [i for i in common_index if list1.count(i) > 0 and list2.count(i) > 0 and list3.count(i) > 0]
```


The function `extract_index_list(list1, list2, list3)` takes three lists as input and returns a list of common elements. The common elements are those that appear in all three lists under the same index. It uses the `set` data structure to find the common elements. Then, it uses list comprehension to filter the common elements based on their frequency in the three lists. The function assumes that the input lists do not contain duplicate elements. If the lists can contain duplicates, the function should be modified to handle this case. The unit test `assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]` checks if the function returns the correct result for the given input.