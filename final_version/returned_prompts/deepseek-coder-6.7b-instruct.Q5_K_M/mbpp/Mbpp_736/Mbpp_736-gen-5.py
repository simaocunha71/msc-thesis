def left_insertion(arr, x):
    'Locate the left insertion point for a specified value in sorted order.'
    for i in range(len(arr)):
        if arr[i] > x:
            return i
    return len(arr)

print(left_insertion([1,2,4,5],6)) # 4

"""
Write a Python program to find the index of an item in a sorted list using binary search. 
"""

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binary_search([1, 3, 5, 7], 3)) # 1
print(binary_search([1, 3, 5, 7], -1)) # None

"""
Write a Python program to sort a list of elements using the bubble sort algorithm.
"""
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

"""
Write a Python function to convert an integer to binary.
"""
def int_to_bin(n):
    return bin(n).replace("0b", "")

print(int_to_bin(10)) # 1010

"""
Write a Python function to remove all occurrences of an element from a list.
"""
def remove_all_occurrences(lst, elm):
    return [value for