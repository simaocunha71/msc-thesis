"""
To solve this, we can use the following steps:

1. Take the first element from each list, and compare them.
2. If the first element from the first list is smaller, add it to the result list. Else, add the first element from the second list to the result list.
3. Repeat step 1 and 2 for all the elements in both the lists. In the end, the result list will have all the elements from both the lists in sorted order.
4. If the size of the result list is odd, return the middle element of the result list. Else, return the average of the two middle elements of the result list.
5. The function should have a time complexity of O(n).
"""

def get_median(list1, list2, n):
    result = []
    i = 0
    j = 0
    while i < n and j < n:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if i < n:
        result.extend(list1[i:])
    else:
        result.extend(list2[j:])

    if len(result) % 2 == 0:
        return (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2.0
    else:
        return result[len(result) // 2]

# Test
print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5)) # 16.0

"""
The time complexity of this solution is O(n) because we are iterating over all the elements of both the lists once.
"""

# If the two lists are not of the same size, you can modify the solution as follows:

def get_median(list1, list2, n):
    result = []
    i = 0
    j = 0
    while i < n and j < len