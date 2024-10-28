You can solve this problem by using a list comprehension to get the lengths of the sublists and then finding the maximum length along with its corresponding sublist.

Here is the Python solution:

```python
def max_length(list_of_lists):
    max_len = max(len(sublist) for sublist in list_of_lists)
    max_sublist = [sublist for sublist in list_of_lists if len(sublist) == max_len][0]
    return (max_len, max_sublist)
```

This function works by first finding the maximum length of the sublists in the list of lists using a generator expression. It then uses a list comprehension to find the sublist with this maximum length. The function returns a tuple containing the maximum length and the corresponding sublist.

The unit test `assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])` ensures that the function works correctly. It checks that the function returns the maximum length (3) and the corresponding sublist ([13, 15, 17]) for the given input. If the function works correctly, this test will pass. If the function does not work correctly, this test will fail. 





# Test the function
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
# Output: (3, [13, 15, 17])  # Passes the test
```





```
# Another example
print(max_length([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
# Output: (4, [6, 7, 8, 9])  # Passes the test
```

This function works correctly for both examples. It returns the maximum length (3 in the first example and 4 in the second example) and the corresponding sublist.