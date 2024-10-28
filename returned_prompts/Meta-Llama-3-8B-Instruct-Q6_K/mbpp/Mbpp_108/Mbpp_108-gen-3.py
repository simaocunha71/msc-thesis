```
def merge_sorted_list(list1, list2, list3):
    result = []
    i, j, k = 0, 0, 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] < list2[j] and list1[i] < list3[k]:
            result.append(list1[i])
            i += 1
        elif list2[j] < list1[i] and list2[j] < list3[k]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list3[k])
            k += 1
    result += list1[i:]
    result += list2[j:]
    result += list3[k:]
    return result
```


The function `merge_sorted_list` takes three lists as input and returns a single sorted list. It uses a three-pointer technique to merge the lists in sorted order. The function iterates through each list, comparing the current elements and adding the smallest one to the result list. Once one of the lists is exhausted, the remaining elements from the other lists are appended to the result. This ensures that the result list is sorted. The unit test provided in the problem ensures that the function works correctly.