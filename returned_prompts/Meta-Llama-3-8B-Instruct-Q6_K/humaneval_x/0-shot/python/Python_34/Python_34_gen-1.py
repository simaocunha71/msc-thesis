def unique(l: list):
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [0, 2, 3, 5, 9, 123]



The function `unique` takes a list `l` as input and returns a new list containing the unique elements from the input list, in sorted order. 

The function uses the built-in `set` function to convert the list to a set, which automatically removes any duplicate elements. The `sorted` function is then used to sort the set in ascending order. 

The test case at the end shows that the function correctly returns the sorted unique elements from the input list. 





