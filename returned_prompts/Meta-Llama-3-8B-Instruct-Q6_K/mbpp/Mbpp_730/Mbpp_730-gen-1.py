def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])) 
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

This function iterates over the list and adds each element to the result list only if it is not equal to the last element in the result list. This effectively removes consecutive duplicates. The function returns the result list. The unit test provided ensures that the function works correctly. 





