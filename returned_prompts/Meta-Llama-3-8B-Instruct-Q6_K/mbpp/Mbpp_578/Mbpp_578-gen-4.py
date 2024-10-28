```
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result
```
This function takes three lists of the same length as input and returns a single flat list where elements from each input list are interleaved. It does this by iterating over the input lists using a for loop, appending the current element from each list to the result list in sequence. The result list is then returned. The unit test provided in the question ensures that the function works correctly for lists of length 7. For lists of any length, this function will work correctly as long as the lists have the same length. If the lists have different lengths, the function will raise an IndexError when it tries to access an element from a shorter list. You could add error checking to handle this case if necessary. 





```
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(max(len(list1), len(list2), len(list3))):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
        if i < len(list3):
            result.append(list3[i])
    return result
```
This version of the function uses the max function to get the maximum length of the three lists. It then iterates over this range, appending elements from each list to the result list in sequence, as long as the current index is within the bounds of the list. This ensures that the function will work correctly even if the lists have different lengths. If a list is shorter than the others, it will simply stop appending elements from that list when it reaches the end of the list. 