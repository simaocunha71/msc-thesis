from collections import Counter

def frequency_lists(arr):
    return Counter(item for sublist in arr for item in sublist)




"""
This function works by utilizing Python's built-in Counter class from the collections module.
The Counter class is designed specifically for counting the frequency of elements in a collection.
The function takes in a list of lists (arr), and uses a list comprehension to flatten the list of lists into a single list.
The list comprehension iterates over each sublist in the original list, and then iterates over each item in the sublist.
The resulting list is then passed to the Counter function, which returns a dictionary with the elements as keys and their frequencies as values.
The function returns this dictionary as the output.
"""




# Sample usage
print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))  # Output: {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

"""
The Counter class is a convenient tool for counting the frequency of elements in a collection, and can be used to solve this problem efficiently.
The function uses a list comprehension to flatten the input list of lists, and then passes the result to the Counter function, which returns the desired dictionary of frequencies.
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

