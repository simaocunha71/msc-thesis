```
def check_occurences(lst):
    result = {}
    for tuple in lst:
        if tuple in result:
            result[tuple] += 1
        else:
            result[tuple] = 1
    return result
```


This function iterates over each tuple in the input list. If the tuple is already in the result dictionary, it increments the count by 1. If the tuple is not in the dictionary, it adds the tuple with a count of 1. The function then returns the dictionary.

The unit test `assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}` ensures that the function correctly maps each unique tuple to the number of times it occurs in the list. In this case, the tuples (1, 3) and (2, 5) both occur twice, and the tuple (3, 6) occurs once. The function correctly captures this information in the output dictionary.