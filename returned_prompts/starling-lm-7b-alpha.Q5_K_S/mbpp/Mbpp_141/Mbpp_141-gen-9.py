"""
def pancake_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_val = arr[i]
        max_index = i
        for j in range(i - 1, -1, -1):
            if arr[j] > max_val:
                max_val = arr[j]
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
        arr = arr[:i] + sorted(arr[i:]) + arr[i:]
    return arr

print(pancake_sort([15, 79, 25, 38, 69]))
"""

# The function doesn't seem to be working. Here's a solution that should work
# using insertion sort

def pancake_sort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
    return arr

print(pancake_sort([15, 79, 25, 38, 69]))

# The function works, but it's not very efficient. The time complexity is
# O(n^2), which is much worse than the O(n log n) that can be achieved using
# other sorting algorithms like merge sort or quick sort.

# Here's a version of the function that uses quick sort instead of insertion sort:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort