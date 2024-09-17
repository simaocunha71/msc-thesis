```
def merge_sorted_list(list1, list2, list3):
    merged_list = []
    i, j, k = 0, 0, 0
    
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] <= list2[j] and list1[i] <= list3[k]:
            merged_list.append(list1[i])
            i += 1
        elif list2[j] <= list1[i] and list2[j] <= list3[k]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list3[k])
            k += 1
            
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
        
    while k < len(list3):
        merged_list.append(list3[k])
        k += 1
        
    return merged_list
```


This function merges three sorted lists into a single sorted list. It uses three pointers to iterate over the three lists and compares the current elements of the three lists to determine which one should be appended to the merged list. If a list is exhausted, the function simply appends the remaining elements of the other lists to the merged list. The function returns the merged list.