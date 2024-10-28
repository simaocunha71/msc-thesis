
```python
def triples_sum_to_zero(l: list):
    length = len(l)
    if length < 3:
        return False
    l.sort()
    for i in range(length - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        start = i + 1
        end = length - 1
        while start < end:
            sum = l[i] + l[start] + l[end]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                return True
    return False
```

In the above code, we first check if the list has less than 3 elements, in which case we return False. Then we sort the list in ascending order. We then iterate over the list using the outer loop. The inner loop uses two pointers, one starting from the next element to the current one and the other starting from the end of the list. We then check if the sum of the three elements is less than, equal to, or greater than 0. If it is less than 0, we increment the start pointer, if it is greater than 0, we decrement the end pointer. If the sum equals 0, we return True. If we have iterated through the entire list without finding a triplet that sums to 0, we return False.

The time complexity of this solution is O(n^2) as there are two nested loops. The space complexity is O(1) as no additional space is used.

Note: This solution assumes that the input list may have duplicate elements. If the list is guaranteed to be without duplicates, the solution can be optimized to O(n^2) time complexity by removing the check for duplicate elements.

Also note that this solution assumes that the input list is not guaranteed to be sorted. The sorting step is necessary for the solution to work correctly.

Also note that this solution assumes that the input list may have negative numbers. If the list is guaranteed to be without negative numbers, the solution can be optimized by removing the check for negative numbers.

Finally, note that this solution assumes that the input list may have zero. If the list is guaranteed to be without zero, the solution can be