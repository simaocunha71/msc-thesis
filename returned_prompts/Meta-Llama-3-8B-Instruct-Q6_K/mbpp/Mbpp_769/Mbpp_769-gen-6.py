You can use the set difference operation to get the difference between two lists in Python. Here's how you can do it:

```Python
def Diff(list1, list2):
    return (list(set(list1) - set(list2)) + list(set(list2) - set(list1)))
```
This function converts the lists to sets, then calculates the difference between the two sets. The result is a set of elements that are in the first list but not in the second. 

The function also calculates the difference between the second list and the first list. The result is a set of elements that are in the second list but not in the first. 

Finally, the function combines these two sets into a single set and converts it back to a list.

The unit test `assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]` shows that the function should return all elements that are in the first list but not in the second, and all elements that are in the second list but not in the first. 

This function does not preserve the order of the elements, which might be a problem if the order matters. If the order matters, you would need a different approach. 

Here is a version of the function that preserves the order of the elements:

```Python
def Diff(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
```
This function uses list comprehensions to create two lists: one for the elements that are in list1 but not in list2, and one for the elements that are in list2 but not in list1. It then combines these two lists into a single list and returns it. This function preserves the order of the elements. 

This function also has a time complexity of O(n*m), where n is the length of list1 and m is the length of list2. This is because it needs to iterate over list1 and list2 to find the elements that are in one list but not the other. If the lists are very large, this function could be slow. If you need a more efficient solution, you would need a different approach. 

In that case, you could sort the lists first, then iterate over them to find the elements that are in one list but not the