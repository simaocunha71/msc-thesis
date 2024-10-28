```
def consecutive_duplicates(lst):
    if not lst:
        return lst
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            result.append(lst[i])
    return result
```
This function iterates over the list, and for each element, it checks if it's different from the previous one. If it is, it adds the element to the result list. If it's not, it skips the element. The function starts by checking if the list is empty, in which case it returns an empty list. If the list is not empty, it starts by adding the first element to the result list. It then iterates over the rest of the list, comparing each element to the previous one, and adding it to the result list if it's different. Finally, it returns the result list. 

For example, if the input list is `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]`, the function will return `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`. The consecutive duplicates of `6` and `4` have been removed. 





