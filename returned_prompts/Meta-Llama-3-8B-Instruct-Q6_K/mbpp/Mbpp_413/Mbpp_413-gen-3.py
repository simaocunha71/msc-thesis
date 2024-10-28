```
def extract_nth_element(lst, n):
    return [tup for i, tup in enumerate(lst) if i == n]
```


This function uses list comprehension to iterate over the list of tuples and return the nth element. The `enumerate` function is used to get both the index and the value of each tuple in the list. The condition `i == n` filters the list to only include the nth element. The function can be tested with the provided unit test.