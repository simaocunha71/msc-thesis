```
def max_length(list_of_lists):
    max_len = max(len(lst) for lst in list_of_lists)
    max_list = [lst for lst in list_of_lists if len(lst) == max_len][0]
    return (max_len, max_list)
```


The function `max_length` takes a list of lists as an argument. It first finds the maximum length of the lists in the list of lists using a generator expression. Then, it finds the list with this maximum length using a list comprehension and the index operator. The function returns a tuple containing the maximum length and the list with this maximum length. 

For example, the function can be used to find the list of maximum length in the list `[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]`. The function will return `(3, [13, 15, 17])`, indicating that the list `[13, 15, 17]` has the maximum length of 3. 

The unit test `assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])` ensures that the function works correctly for this specific input. 

Note that the list comprehension `[lst for lst in list_of_lists if len(lst) == max_len][0]` will raise an IndexError if there are multiple lists with the maximum length. In this case, you may want to modify the function to return all lists with the maximum length, or to raise a more specific exception. 