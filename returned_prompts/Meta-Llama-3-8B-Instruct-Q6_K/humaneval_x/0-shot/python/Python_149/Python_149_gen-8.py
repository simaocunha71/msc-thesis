```
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    even_length_list = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    sorted_list = sorted(even_length_list, key=lambda s: (len(s), s))
    
    return sorted_list
```


Solution:

The problem is asking you to create a function that accepts a list of strings, removes the strings with odd lengths, and returns the resulting list in sorted order. The list should be sorted first by the length of each word and then alphabetically. 

Here's how you can solve it:

1. First, you need to filter out the strings with odd lengths. You can do this using a list comprehension. 

2. Next, you need to sort the list. You can use the built-in `sorted` function for this. The `sorted` function takes a key function as an argument, which it uses to determine the sort order. In this case, you can use a lambda function that returns a tuple. The first element of the tuple is the length of the string, and the second element is the string itself. This will sort the list first by length and then alphabetically.

Here's the complete code:

```
def sorted_list_sum(lst):
    even_length_list = [s for s in lst if len(s) % 2 == 0]
    sorted_list = sorted(even_length_list, key=lambda s: (len(s), s))
    return sorted_list
```

This function works by first creating a new list `even_length_list` that contains only the strings with even lengths. It then sorts this list using the `sorted` function, and returns the sorted list. The `sorted` function uses the lambda function as its key function, which tells it to sort the list first by length and then alphabetically. 

For example, if you call `sorted_list_sum(["aa", "a", "aaa"])`, the function will return `["aa"]`. If you call `sorted_list_sum(["ab", "a", "aaa", "cd"])`, the function will return `["ab", "cd"]`. 

The function works correctly because it first removes the strings with odd lengths, then sorts the remaining strings by length and alphabetically, and finally returns the sorted list. 

The unit tests provided ensure that the function works correctly. For example, the test `assert list_sort(["aa