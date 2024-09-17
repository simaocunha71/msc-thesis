```
def pack_consecutive_duplicates(lst):
    result = []
    temp = []
    for i in lst:
        if not temp or i != temp[-1]:
            if temp:
                result.append(temp)
            temp = [i]
        else:
            temp.append(i)
    if temp:
        result.append(temp)
    return result
```    
Explanation:
The function `pack_consecutive_duplicates` takes a list as an input and returns a new list where consecutive duplicates are packed into sublists. It iterates over the input list, and for each element, it checks if it's different from the last element in the current sublist (if any). If it's different, it adds the current sublist to the result list and starts a new sublist with the current element. If it's the same, it adds the current element to the current sublist. Finally, it adds the last sublist to the result list if necessary. The function returns the result list. 

For example, the input list `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]` will be converted to `[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]`. The unit test `assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]` ensures that the function works correctly. 