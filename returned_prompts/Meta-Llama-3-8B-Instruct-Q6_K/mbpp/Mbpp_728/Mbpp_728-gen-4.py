```
def sum_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be the same length")
    return [a+b for a, b in zip(list1, list2)]
```


The function sum_list takes two lists as input. It first checks if the two lists are the same length. If they are not, it raises a ValueError. If they are the same length, it uses a list comprehension to create a new list where each element is the sum of the corresponding elements from the input lists. This is done using the zip function, which pairs up the elements from the two lists, and the list comprehension, which adds each pair of elements together. The result is a new list where each element is the sum of the corresponding elements from the input lists. 

For example, if we call sum_list([10,20,30],[15,25,35]), the function will return [25,45,65], which is the sum of the corresponding elements from the input lists.  The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` ensures that the function works correctly. 

This function is case-insensitive and works with lists of any length. If the input lists are empty, the function will return an empty list. 

The time complexity of this function is O(n), where n is the length of the input lists, because it needs to iterate over the elements of the lists once. The space complexity is also O(n), because it needs to create a new list to store the results. 