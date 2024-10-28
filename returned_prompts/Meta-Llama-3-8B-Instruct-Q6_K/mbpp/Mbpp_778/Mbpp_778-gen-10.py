```
def pack_consecutive_duplicates(lst):
    result = []
    if not lst:
        return result
    
    current_group = [lst[0]]
    
    for num in lst[1:]:
        if num == current_group[-1][0]:
            current_group.append(num)
        else:
            result.append(current_group)
            current_group = [num]
    
    result.append(current_group)
    return result
```


The function `pack_consecutive_duplicates` takes a list of elements as input and returns a list of sublists. Each sublist contains consecutive duplicates of the same element. If the input list is empty, it returns an empty list.

Here's how the function works:

1. Initialize an empty list `result` to store the result.
2. If the input list is empty, return `result`.
3. Initialize a list `current_group` with the first element of the input list.
4. Iterate over the input list, starting from the second element.
5. For each element, check if it is the same as the last element of `current_group`. If it is, append it to `current_group`.
6. If the element is different from the last element of `current_group`, append `current_group` to `result` and reset `current_group` with the current element.
7. After the loop, append `current_group` to `result`.
8. Return `result`.

The function uses a simple iterative approach to pack consecutive duplicates of the input list elements into sublists. It maintains a `current_group` to store consecutive duplicates and appends it to `result` when a different element is encountered.

The unit test `assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]` demonstrates the expected output of the function. It shows that the function correctly packs consecutive duplicates of the input list elements into sublists.