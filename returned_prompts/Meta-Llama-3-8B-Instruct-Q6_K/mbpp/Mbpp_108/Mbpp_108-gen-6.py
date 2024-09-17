```
def merge_sorted_list(list1, list2, list3):
    result = []
    while len(list1) > 0 and len(list2) > 0 and len(list3) > 0:
        if list1[0] <= list2[0] and list1[0] <= list3[0]:
            result.append(list1.pop(0))
        elif list2[0] <= list3[0]:
            result.append(list2.pop(0))
        else:
            result.append(list3.pop(0))
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    return result
```


The function takes three lists as input and merges them into a single sorted list. It does this by comparing the first elements of each list and adding the smallest one to the result list. This process is repeated until one of the lists is empty. Finally, the remaining elements in the other lists are added to the result list. The function returns the merged and sorted list. 

The unit test provided shows the expected output for a specific set of inputs. The function is tested with these inputs and should return the expected output. 

The time complexity of this function is O(n log n) where n is the total number of elements in the three lists, because it involves sorting the lists. The space complexity is O(n) for the result list. 

This function assumes that the input lists are sorted. If the lists are not sorted, the function will not work correctly. If the lists contain duplicate elements, the function will also not work correctly because it does not preserve the order of duplicate elements. 

It's worth noting that this function does not handle the case where the input lists are empty. If the input lists are empty, the function will return an empty list. If the function should handle empty lists, it should check for this case and return an appropriate result. 

This function is not efficient for large lists because it involves sorting the lists. A more efficient solution would be to use the heapq.merge function from the heapq module, which can merge multiple sorted inputs into a single sorted output. This function has a time complexity of O(n) and a space complexity of O(n), where n is the total number of elements in the input lists. 

Here is the modified function using heapq.merge:
```
import heapq

def merge_sorted_list(list1, list2, list3):
    return list(heapq.merge(list1, list2, list3))
```
