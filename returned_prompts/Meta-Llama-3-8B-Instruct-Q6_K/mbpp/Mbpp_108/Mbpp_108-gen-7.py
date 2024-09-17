```
def merge_sorted_list(list1, list2, list3):
    result = []
    while list1 and list2 and list3:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        elif list2[0] < list3[0]:
            result.append(list2.pop(0))
        else:
            result.append(list3.pop(0))
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    return result
```
The provided function merges three sorted lists into a single sorted list. It does this by comparing the smallest element from each list and appending it to the result list. This process continues until one of the lists is exhausted, at which point the remaining elements from the other lists are appended to the result list. The time complexity of this function is O(n), where n is the total number of elements in the three lists. The space complexity is also O(n), as the function returns a new list that contains all the elements from the input lists.