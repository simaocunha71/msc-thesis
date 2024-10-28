```
def count_element_in_list(lst, element):
    return sum(1 for sub in lst if element in sub)
```


This function works by iterating over each sublist in the given list and checking if the given element is present in that sublist. If the element is present, it counts it and adds 1 to the total count. Finally, it returns the total count. This function is used to solve the problem by counting the number of sublists containing a particular element. The unit test provided helps in understanding the problem better. It checks if the function correctly counts the number of sublists containing the element 1 in the given list. The function should return 3 in this case, which it does. 





This solution passes the test case:

```
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
```





The time complexity of this function is O(n*m) where n is the number of sublists and m is the maximum size of a sublist. This is because it needs to iterate over each element in each sublist to check if the given element is present. The space complexity is O(1) as it only uses a constant amount of space to store the count.