def pancake_sort(lst):
    for i in range(len(lst), 0, -1):
        max_index = lst[0:i].index(max(lst[0:i]))
        if max_index != i - 1:
            lst[0:i] = lst[0:i][::-1]
            lst[0:i] = lst[0:i][::-1]
    return lst

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
Explanation:
Here we use the concept of pancake sorting, a sorting method where we flip the elements in the array in-place. We find the maximum element in the unsorted part of the array and flip it to the beginning. Then we flip the unsorted part to its correct position. We continue this process until the array is sorted.
"""

# Test cases
assert pancake_sort([3, 2, 4, 1]) == [1, 2, 3, 4]
assert pancake_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
assert pancake_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
assert pancake_sort([1]) == [1]
assert pancake_sort([]) == []
assert pancake_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
assert pancake_sort([2, 1, 4, 3]) == [1, 2, 3, 4]
assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert pancake_sort([1, 2, 1, 2]) == [1, 1, 2, 2]
assert pancake_sort([5,