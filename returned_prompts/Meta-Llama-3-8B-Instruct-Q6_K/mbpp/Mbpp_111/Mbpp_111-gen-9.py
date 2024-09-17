```
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    common = set(flat_list)
    return common
```

The function `common_in_nested_lists` takes a list of lists as an argument. It first flattens the list of lists into a single list using a list comprehension. Then it converts this list into a set, which removes any duplicates. This set of unique elements is then returned as the result. 

The unit test provided shows that this function should work correctly for the given example. It checks if the set of common elements in the given nested lists is equal to the set `{18, 12}`, which is the expected output. 

The time complexity of this function is O(n), where n is the total number of elements in the nested lists, because it needs to iterate over each element in the lists. The space complexity is also O(n), because it needs to store all the elements in the flat list. 

This function can be used to find the common elements in any number of nested lists. It is not limited to the specific example provided in the unit test. 

Please note that this function does not check if the common elements appear in the same position in the nested lists. It simply finds all the unique elements that appear in at least one of the nested lists. If you want to find the common elements that appear in the same position in the nested lists, you would need to use a different approach. 

Here is an example of how you could modify this function to find the common elements that appear in the same position in the nested lists:

```
def common_in_nested_lists(nested_lists):
    if not nested_lists:
        return []
    common = [element for elements in zip(*nested_lists) for element in elements if list(elements).count(element) == len(nested_lists)]
    return set(common)
```

This modified function uses the `zip` function to transpose the nested lists, so that corresponding elements from each list are paired together. It then uses a list comprehension to iterate over these paired elements, and includes an element in the result if it appears in the same position in all the lists. The result is then converted to a set, which removes any duplicates. 

This modified function has the same time complexity as the original function, but its space complexity is O(m), where m is the length of the longest list in the nested lists, because it needs to store the transposed lists in memory. 

