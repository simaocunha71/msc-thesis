```
def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```


The function `sorted_list_sum(lst)` takes a list of strings as input, filters out the strings with odd lengths, and then sorts the remaining strings based on their lengths and alphabetical order. 

The list comprehension `[word for word in lst if len(word) % 2 == 0]` is used to create a new list that includes only the strings with even lengths.

The `sort()` method is then used to sort the list of strings. The `key` argument is a function that takes a list element and returns a value that will be used for sorting purposes. In this case, the `key` function is a lambda function that returns a tuple. The first element of the tuple is the length of the string, and the second element is the string itself. This means that the list will be sorted first by the length of the strings, and then by alphabetical order.

For example, if the input list is `["aa", "a", "aaa", "cd"]`, the function will first filter out the strings with odd lengths, leaving `["aa", "aaa", "cd"]`. It will then sort this list by the length of the strings (first "aa" and "aaa" because they have the same length, then "aaa" because it is alphabetically smaller) and then by alphabetical order (first "aa" and then "aaa" and "cd"). The final output will be `["aa", "cd"]`. 





Test cases:
```
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```


The function passes the test cases. It correctly filters out the strings with odd lengths, sorts the remaining strings by their lengths and alphabetical order, and returns the result as a list of strings. 