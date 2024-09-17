The problem is asking to write a function that takes two lists as input and returns a list of elements that are present in either list but not in both. The order of elements in the result list does not matter.

The unit test provided suggests that the function should return the elements that are present in the first list but not in the second list, followed by the elements that are present in the second list but not in the first list.

Here is a Python function that solves the problem:
```
def Diff(list1, list2):
    return list(set(list1) - set(list2)) + [x for x in list2 if x not in set(list1)]
```
This function uses the set data structure to find the elements that are present in either list but not in both. The `set(list1) - set(list2)` expression finds the elements that are present in `list1` but not in `list2`, and the `[x for x in list2 if x not in set(list1)]` expression finds the elements that are present in `list2` but not in `list1`. The two lists are then concatenated to form the final result.