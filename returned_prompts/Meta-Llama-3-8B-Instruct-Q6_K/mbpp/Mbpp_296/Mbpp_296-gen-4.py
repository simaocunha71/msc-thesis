```
def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half_count = get_Inv_Count(left_half)
    right_half_count = get_Inv_Count(right_half)

    merged_count = merge_and_count(left_half, right_half)

    return left_half_count + right_half_count + merged_count


def merge_and_count(left, right):
    merged = []
    inv_count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return inv_count
```

Explanation:
The problem is asking to count the number of inversions in an array, which is defined as a pair of elements that are in the wrong order (i.e., a > b). The function `get_Inv_Count` recursively divides the array into two halves, counts the inversions in each half, and then merges the two halves while counting the inversions that occur during the merge process.

The `merge_and_count` function takes two sorted lists as input and merges them into a single sorted list. It also counts the inversions that occur during the merge process. An inversion occurs when an element from the right list is smaller than an element from the left list, which means that the element from the right list should be placed before the element from the left list in the sorted output.

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` checks that the function correctly counts the inversions in the given array. The array has 5 inversions: (20,1), (20,6), (20,4), (6,4), and (5,4). The function should return 5, which it does.