def heap_sort(lst):
    # Convert list into heap
    for i in range(len(lst)):
        heapify(lst, len(lst), i)
    # One by one extract elements
    for i in range(len(lst)-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i] # swap
        heapify(lst, i, 0)
    return lst

def heapify(lst, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    # See if left child of root exists and is greater than root
    if l < n and lst[i] < lst[l]:
        largest = l
    # See if right child of root exists and is greater than root
    if r < n and lst[largest] < lst[r]:
        largest = r
    # Change root if needed
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]  # swap
        # Heapify the root.
        heapify(lst, n, largest)

print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
"""


"""
