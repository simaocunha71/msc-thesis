def consecutive_duplicates(lst):
    """
    Remove consecutive duplicates from a given list.
    """
    if not lst:
        return []
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result

# Test
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```
1
 
2
3
4
5
6
7
8
9
10
```

The `consecutive_duplicates` function takes a list `lst` as input. It first checks if the list is empty, and if so, it returns an empty list. 

Then, it initializes an empty list called `result` to store the unique elements from the input list. 

Next, it iterates through the input list using a for loop. For each element in the list, it checks if it's the first element or if it's different from the previous element. If either of these conditions is true, it appends the current element to the `result` list. 

Finally, it returns the `result` list containing the unique elements from the input list. 

The provided test case `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]` is passed, indicating that the function correctly removes consecutive duplicates from the given list.
```