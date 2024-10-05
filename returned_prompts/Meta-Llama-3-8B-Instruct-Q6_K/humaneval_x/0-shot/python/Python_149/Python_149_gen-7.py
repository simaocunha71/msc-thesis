```
def sorted_list_sum(lst):
    lst = [s for s in lst if len(s) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```


This function first filters out the strings with odd lengths using a list comprehension. Then it sorts the list using the built-in sort method, with a key function that returns a tuple. The first element of the tuple is the length of the string, and the second element is the string itself. This means that the list will be sorted first by the length of the strings, and then by the strings themselves in alphabetical order. Finally, the function returns the sorted list. 

The unit test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` suggests that the function should return a list with only strings that have even lengths, which is what this function does. The unit test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` suggests that the function should sort the list first by the length of the strings, and then by the strings themselves in alphabetical order, which is also what this function does. 

Note that the function does not actually calculate the sum of the strings, it just sorts the list of strings. If you want to calculate the sum of the strings, you would need to modify the function to do that. However, the problem statement does not mention calculating the sum of the strings, so I assume that is not what you want. 