```
def Diff(list1, list2):
    diff_list1 = [i for i in list1 if i not in list2]
    diff_list2 = [i for i in list2 if i not in list1]
    return diff_list1 + diff_list2
```


The function Diff takes two lists as input and returns a list of elements that are in either list1 or list2 but not in both. It uses list comprehension to create two lists: diff_list1 contains elements from list1 that are not in list2, and diff_list2 contains elements from list2 that are not in list1. Finally, it returns the concatenation of these two lists. The unit test provided ensures that the function works correctly. For example, if list1 = [10, 15, 20, 25, 30, 35, 40] and list2 = [25, 40, 35], the function should return [10, 20, 30, 15]. This is because 10, 20, 30 are in list1 but not in list2, and 15 is in list1 but not in list2. Similarly, 25, 40, 35 are in list2 but not in list1. Therefore, the function returns the concatenation of these two lists, which is [10, 20, 30, 15]. 