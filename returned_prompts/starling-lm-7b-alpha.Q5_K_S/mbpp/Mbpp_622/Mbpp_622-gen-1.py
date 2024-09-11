To find the median of two sorted lists of same size, you can follow these steps:

1. Combine the two lists into a single sorted list. If the combined list has an odd number of elements, the median is the middle element. If it has an even number of elements, the median is the average of the two middle elements.

2. To merge the two sorted lists, you can use the concept of two pointers. Initialize two pointers, one at the start of each list. Compare the elements at the current positions of the pointers. The smaller element is added to the result list, and the pointer is moved forward. Repeat this process until one of the lists is fully traversed. The remaining elements in the other list are added to the result list.

3. After merging the two lists, if the length of the combined list is odd, the median is the element at the middle index. If the length is even, the median is the average of the elements at the middle index and the index before it.

Here's an example implementation of the get_median function in Python:

```python
def get_median(list1, list2, n):
    merged_list = []
    idx1 = idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            merged_list.append(list1[idx1])
            idx1 += 1
        else:
            merged_list.append(list2[idx2])
            idx2 += 1
    merged_list.extend(list1[idx1:] + list2[idx2:])
    n = len(merged_list)
    if n % 2 == 0:
        return (merged_list[n//2 - 1] + merged_list[n//2]) / 2
    else:
        return merged_list[n//2]
```

You can use the function like this:

```python
print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))  # Output