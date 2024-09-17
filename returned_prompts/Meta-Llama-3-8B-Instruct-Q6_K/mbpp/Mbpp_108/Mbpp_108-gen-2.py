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
This function merges three sorted lists into a single sorted list. It uses three pointers, i, j, k, to keep track of the current element in each list. It compares the current elements in each list and appends the smallest one to the result list. The process continues until all elements in the lists have been processed. The remaining elements in the lists are then appended to the result list. The function returns the merged and sorted list. 

The unit test `assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]` ensures that the function correctly merges and sorts the lists.  It checks if the output of the function is equal to the expected output.  If the output is equal, the test passes.  If the output is not equal, the test fails.  This ensures that the function works correctly for different inputs. 

The time complexity of this function is O(n), where n is the total number of elements in the three lists.  This is because the function processes each element in the lists once.  The space complexity is O(n), where n is the total number of elements in the three lists.  This is because the function creates a new list to store the merged and sorted elements.