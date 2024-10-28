
Explanation:

1. First, we check if the list is empty. If it is, we return None because there are no elements to find the 2nd smallest.
2. We find the minimum value in the list using the min() function.
3. We check if there are more than one occurrences of the minimum value in the list. If there are, it means the list has duplicate values and the 2nd smallest element does not exist. In this case, we return None.
4. Finally, we create a new list that includes all elements in the original list that are greater than the minimum value. We then return the minimum value of this new list, which is the 2nd smallest element in the original list.

Note: The time complexity of this solution is O(n), where n is the length of the input list, because we need to iterate over the list twice (once to find the minimum value and once to create the new list). The space complexity is O(n) as well, because we need to store the new list. However, we can improve the space complexity to O(1) by using a single loop to find both the minimum value and the 2nd smallest element. Here is the improved solution:

```
def next_smallest(lst):
    if not lst:
        return None
    min_val = float('inf')
    second_smallest = None
    for num in lst:
        if num < min_val:
            second_smallest = min_val
            min_val = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != min_val else None
```

This solution has the same time complexity as the previous one, but it has a space complexity of O(1) because it only uses a constant amount of space to store the minimum and second smallest values. It also handles the case where the list has duplicate values correctly.