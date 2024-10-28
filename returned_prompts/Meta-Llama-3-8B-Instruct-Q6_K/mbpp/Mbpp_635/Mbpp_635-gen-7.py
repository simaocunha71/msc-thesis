```
def heap_sort(lst):
    heap = list(lst)
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, i, len(heap))
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)
    return heap

def heapify(heap, i, n):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and heap[l] > heap[largest]:
        largest = l
    if r < n and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest, n)
```
This solution uses the heap sort algorithm to sort the given list. The heapify function is used to maintain the heap property of the heap. The heapify function works by comparing the node at index i with its left and right children. If the left or right child is larger, it swaps the node with the child and recursively calls itself on the child. The heapify function is called on each node in the heap to ensure that the heap property is maintained. The heap is then iteratively reduced to the smallest element, which is swapped with the last element of the heap, and the heapify function is called again to maintain the heap property. This process is repeated until the heap is empty, resulting in a sorted list. The sorted list is then returned. The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` confirms that the function is working correctly.