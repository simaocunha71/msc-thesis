def check_min_heap(arr):
    for i in range(len(arr)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(arr) and arr[left_child] < arr[i]:
            return False
        if right_child < len(arr) and arr[right_child] < arr[i]:
            return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6])) # True


"""
Write a function to check if the given array represents max heap or not. 
assert check_max_heap([9, 8, 7, 6, 5, 4]) == True
"""

def check_max_heap(arr):
    for i in range(len(arr)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(arr) and arr[left_child] > arr[i]:
            return False
        if right_child < len(arr) and arr[right_child] > arr[i]:
            return False
    return True

print(check_max_heap([9, 8, 7, 6, 5, 4])) # True

"""
Write a Python function to sort a list using the heap sort algorithm.
assert heap_sort([4, 3, 2, 10, 12, 1, 5, 6]) == [1, 2, 3, 4, 5, 6, 10, 12]
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest