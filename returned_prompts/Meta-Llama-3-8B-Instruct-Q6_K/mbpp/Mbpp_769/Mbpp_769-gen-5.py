```
def Diff(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    diff1 = list(set1 - common)
    diff2 = list(set2 - common)
    return diff1 + diff2
```

This function works by first converting the input lists into sets. It then finds the common elements between the two sets using the & operator. The - operator is used to find the elements that are in one set but not the other. These elements are then converted back into lists and concatenated to form the final result. 

For example, if we call `Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])`, the function will return `[10, 20, 30, 15]`, which is the difference between the two input lists. 

The unit test `assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]` ensures that the function is working correctly. 

This function assumes that the input lists do not contain duplicate elements. If the lists can contain duplicates and the order of the elements in the output list does not matter, then this function will still work correctly. However, if the order of the elements in the output list does matter and the input lists can contain duplicates, then a different approach would be needed. 

For example, if the input lists can contain duplicates and the order of the elements in the output list matters, then we could use a list comprehension to create the output list. Here is an example:
```
def Diff(list1, list2):
    return [x for x in list1 + list2 if (x in list1 and x not in list2) or (x not in list1 and x in list2)]
```
This function works by iterating over the concatenation of the two input lists and including an element in the output list if it is in one of the input lists but not the other. The order of the elements in the output list is the same as the order in which they appear in the input lists. 

However, this function is less efficient than the original function because it has to iterate over the concatenation of the two input lists, which can be slow if the lists are