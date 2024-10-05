```
def sorted_list_sum(lst):
    # Filter the list to only include strings with even lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list based on the length of each string
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings
```

This function works by first creating a new list that includes only the strings from the input list that have even lengths. It does this using a list comprehension and the modulus operator (`%`), which returns the remainder of the division of the string's length by 2. If the remainder is 0, the length is even.

Next, it sorts the list of strings based on the length of each string. If two strings have the same length, it sorts them alphabetically. It does this using the `sorted` function with a lambda function as the `key` argument. The lambda function returns a tuple for each string, where the first element of the tuple is the length of the string and the second element is the string itself. The `sorted` function then sorts the list based on these tuples, so strings with shorter lengths come first, and if two strings have the same length, the one that comes first alphabetically comes first.

Finally, it returns the sorted list of strings.