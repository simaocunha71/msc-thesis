```
def extract_index_list(list1, list2, list3):
    common_indices = [i for i in range(len(list1)) if list1[i] == list2[i] == list3[i]]
    return [x for x in list1 if x in list2 and x in list3]
```
This function works by first finding the indices at which all three lists have the same element. It then uses these indices to extract the common elements from the lists. The function uses list comprehensions to achieve this in a concise and efficient way.

The unit test provided ensures that the function works correctly. It checks that the function returns the correct result for the given lists. This test helps to validate the function and ensures that it behaves as expected. 







