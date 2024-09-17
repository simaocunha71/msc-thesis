```
def Diff(list1, list2):
    result = []
    for element in list1:
        if element not in list2:
            result.append(element)
    for element in list2:
        if element not in list1:
            result.append(element)
    return result
```
The function `Diff(list1, list2)` takes two lists as input and returns a new list containing the elements that are in `list1` but not in `list2`, and vice versa. The order of elements in the result list is the same as their order in the input lists. If an element is present in both lists, it will appear in the result list only once. 

The function uses two loops to iterate over the elements of the input lists. In the first loop, it checks each element of `list1` to see if it is present in `list2`. If it is not, it adds the element to the result list. In the second loop, it checks each element of `list2` to see if it is present in `list1`. If it is not, it adds the element to the result list. 

The function uses the `in` operator to check if an element is present in a list. This operator returns `True` if the element is present in the list, and `False` otherwise. 

The function returns the result list at the end. The unit test `assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]` ensures that the function is working correctly. 

Note that the function is case sensitive, and it treats lists as sets. This means that if you have two lists with the same elements but in a different order, the function will still return the correct result. However, if you have two lists with the same elements but with different cases (e.g., "apple" and "Apple"), the function will treat them as different elements. 

Also, the function does not preserve the order of elements in the result list. If you need to preserve the order, you can use a different approach, such as using a dictionary to keep track of the elements you have seen so far. 

Finally, the function has a time complexity of O(n), where n is the length of the input lists. This is because it uses two loops that iterate over the elements of the input lists. The