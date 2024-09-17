```
def similar_elements(list1, list2):
    return set(x for x in list1 if x in list2)
```


The function takes two lists as input and returns a set of elements that are present in both lists. The set data structure is used to remove duplicates and to provide a fast lookup time for the elements. The function uses a generator expression to iterate over the elements in the first list and checks if each element is also present in the second list. If an element is found in both lists, it is added to the set of similar elements. The function returns this set at the end. 

The unit test `assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))` ensures that the function is working correctly. It checks if the function returns the correct set of elements for the given input lists. If the function is working correctly, the test will pass. If the function is not working correctly, the test will fail and an error message will be displayed, indicating the difference between the expected and actual results. 

This function has a time complexity of O(n), where n is the length of the first list, because it needs to iterate over each element in the first list to check if it is present in the second list. The space complexity is also O(n), because in the worst case, all elements from the first list could be present in the second list, and the function would need to store all these elements in the set. 
```python
def similar_elements(list1, list2):
    return set(x for x in list1 if x in list2)
```


This function takes two lists as input and returns a set of elements that are present in both lists. The set data structure is used to remove duplicates and to provide a fast lookup time for the elements. The function uses a generator expression to iterate over the elements in the first list and checks if each element is also present in the second list. If an element is found in both lists, it is added to the set of similar elements. The function returns this set at the end. 

The unit test `assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))` ensures that the function is working correctly. It checks if the function returns the correct set of elements for the given input lists.