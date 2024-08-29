def get_Inv_Count(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

assert get_Inv_Count([1,20,6,4,5]) == 5

# O(n^2) time complexity, not efficient for large lists

# More efficient solution using Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left[i:])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return (result, inv_count)

def get_Inv_Count_efficient(arr):
    _, inv_count = merge_sort(arr)
    return inv_count

assert get_Inv_Count_efficient([1,20,6,4,5]) == 5

# O(n log n) time complexity, more efficient for large lists.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Given a list of numbers, write a python function to return a list of lists where each sublist is a pair of numbers from the input list that have a difference of 2. The input list may contain duplicate numbers.
<jupyter_code>
