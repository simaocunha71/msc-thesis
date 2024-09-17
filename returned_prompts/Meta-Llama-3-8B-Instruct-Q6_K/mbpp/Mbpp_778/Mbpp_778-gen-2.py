```
def pack_consecutive_duplicates(lst):
    result = []
    i = 0
    while i < len(lst):
        count = 1
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            i += 1
            count += 1
        result.append(lst[i] * count)
        i += 1
    return result
```


This function iterates over the input list, counting consecutive duplicates of each element. When it encounters a different element, it appends the count of the previous element to the result list. The result is a list of lists, where each sublist contains consecutive duplicates of an element from the original list.

For example, given the input `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]`, the function returns `[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]`.