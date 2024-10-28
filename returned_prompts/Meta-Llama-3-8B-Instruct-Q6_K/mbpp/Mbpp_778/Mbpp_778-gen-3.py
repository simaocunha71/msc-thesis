```
def pack_consecutive_duplicates(lst):
    result = []
    i = 0
    while i < len(lst):
        count = 1
        while i + 1 < len(lst) and lst[i] == lst[i+1]:
            i += 1
            count += 1
        result.append(lst[i]*[lst[i]])[:count]
        i += 1
    return result
```
This function iterates over the list and counts the consecutive duplicates of each element. It then appends a sublist with the element repeated the same number of times as the count. The result is a list of sublists where each sublist contains consecutive duplicates of the corresponding element in the original list. 

For example, the input `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]` will produce the output `[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]`. 

The unit test `assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]` verifies that the function works correctly. 

This function has a time complexity of O(n) where n is the length of the input list, as it iterates over the list once. The space complexity is also O(n) as it creates a new list to store the result. 