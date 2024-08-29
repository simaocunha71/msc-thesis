"""
Algorithm:
- Build a max heap from the input data.
- The largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
- Repeat above steps while size of heap is greater than 1.
"""

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heap_sort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
    return arr

print(heap_or_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

"""
OUTPUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

assert heap_sort([1, 3, 5, 7, 9, 2