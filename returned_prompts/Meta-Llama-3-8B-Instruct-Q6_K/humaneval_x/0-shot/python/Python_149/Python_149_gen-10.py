```
def sorted_list_sum(lst):
    lst = [i for i in lst if len(i) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```



The provided unit tests suggest that the function should return a list of strings in sorted order. The order of the list should be ascending by length of each word, and if two words have the same length, the list should be sorted alphabetically. 

Here is a Python function that satisfies these conditions:

```
def sorted_list_sum(lst):
    lst = [i for i in lst if len(i) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```

This function first creates a new list that includes only the strings with even lengths. It then sorts this list using the built-in sort method and a lambda function as the key. The lambda function returns a tuple for each string in the list, where the first element of the tuple is the length of the string and the second element is the string itself. The sort method then sorts the list based on these tuples, first by the length and then by the string itself. The resulting list is then returned. 

For example, if the input list is `["aa", "a", "aaa"]`, the function will return `["aa"]`. If the input list is `["ab", "a", "aaa", "cd"]`, the function will return `["ab", "cd"]`.  These results are consistent with the provided unit tests. 