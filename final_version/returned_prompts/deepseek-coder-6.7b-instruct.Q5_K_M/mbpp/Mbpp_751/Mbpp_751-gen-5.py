def check_min_heap(arr):
    n = len(arr) 
  
    # If last element is greater than its parent,
    # it means the array is not a min heap.
    for i in range(1, n): 
        if arr[i] < arr[(i - 1)//2] : 
            return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6])) # should return True
"""

def check_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6])) # should return True
"""
def check_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6])) # should return True
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([6, 5, 4, 3, 2, 1]) == True
assert check_min_heap([6, 4, 5, 1, 3, 2]) == False
assert check_min_heap([10, 15, 13, 21, 16, 25, 28, 30]) == False
assert check_min_heap([30, 28, 25