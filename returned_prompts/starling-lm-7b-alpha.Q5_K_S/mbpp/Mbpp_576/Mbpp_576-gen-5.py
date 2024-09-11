def is_sub_list(list1, list2):
    for i in range(len(list2)):
        if(list1 == list2[i:i+len(list1)]):
            return True
    return False

# Testing the function
list1 = [1,4,3,5]
list2 = [1,2]
print(is_sub_list(list1, list2))

# Output: False
"""
The above function works by comparing the two lists element by element. It takes two parameters, list1 and list2. It initializes an empty list called list2 and starts a for loop that iterates through each index in list2. Within the loop, it checks if list1 is equal to the subsection of list2, starting from the current index and of the same length as list1. If it is, it returns True. If it isn't and the loop has finished iterating through all of list2, it returns False.
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
