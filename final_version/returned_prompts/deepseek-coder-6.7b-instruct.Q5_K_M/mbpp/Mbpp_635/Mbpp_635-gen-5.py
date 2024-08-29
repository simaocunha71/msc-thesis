def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        sift_down(arr, 0, end)
    return arr

def heapify(arr):
    start = len(arr) // 2 - 1
    while start >= 0:
        sift_down(arr, start, len(arr) - 1)
        start -= 1

def sift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 <= end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap != root:
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap
        else:
            return

print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

"""
heap_sort function firstly calls heapify function to convert list into a heap. Then it starts to sort the list. It swaps the first element of the heap with the last element, and then reduces the size of the heap by one. It continues this until all elements are sorted.

heapify function transforms list into a heap. It starts from the middle of the list and goes towards the start of the list. For each element, it checks if it is smaller than its children, if it is, it swaps the element with the smallest child. It continues this until the heap property is maintained.

sift_down function is used to maintain the heap property after swapping the first element with the last element. It starts from the root of the heap and checks if the root is smaller than its children. If it is, it swaps the root with the smallest child. It continues this until the heap property is maintained.
"""

# Complexity: O(n log n)
