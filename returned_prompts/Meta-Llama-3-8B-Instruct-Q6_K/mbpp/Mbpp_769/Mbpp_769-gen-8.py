```
def Diff(list1, list2):
    return list(set(list1) ^ set(list2))
```  # This function will return the difference between two lists, but it will also return the elements that are in both lists.
For example, Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) will return [10, 15, 20, 30] and also [25, 40, 35] because these are in both lists.

If you want to return only the elements that are in list1 but not in list2, you can use the following function:
```
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]
```
This function will return [10, 15, 20, 30] and will not return [25, 40, 35] because these are in both lists.

If you want to return only the elements that are in list2 but not in list1, you can use the following function:
```
def Diff(list1, list2):
    return [i for i in list2 if i not in list1]
```
This function will return [25, 40, 35] and will not return [10, 15, 20, 30] because these are in both lists.  # This function will return the difference between two lists, but it will also return the elements that are in both lists.
For example, Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) will return [10, 15, 20, 30, 25, 40, 35] because these are in both lists.

If you want to return only the elements that are in list1 but not in list2, you can use the following function:
```
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]
```
This function will return [10, 15, 20, 30] and will not return [25, 40, 35] because these are in both lists.

If you want to return only the elements that are in list2 but not in list1, you can use the following function:
```
def Diff(list1, list2):
    return [