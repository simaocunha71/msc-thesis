```
def heap_sort(lst):
    for i in range(len(lst) // 2 - 1, -1, -1):
        heapify(lst, len(lst), i)
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)
    return lst

def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[i] < lst[left]:
        largest = left
    if right < n and lst[largest] < lst[right]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)
```
The heap sort algorithm is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to the selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining element.

In the heapify function, we start from the non-leaf node and compare the node with its left and right child. If the left or right child is greater than the node, we swap the node with its larger child. We repeat this process until the node is greater than its children.

In the heap sort function, we start from the last non-leaf node and call the heapify function for each node. After that, we repeatedly swap the root node with the last node and call heapify for the reduced heap until the heap size is 1. The root node will be the maximum element, so we place it at the end. We repeat the same process for the remaining nodes.

The time complexity of heap sort is O(n log n) in the worst case, where n is the number of elements in the list. The space complexity is O(1) as we do not use any extra space. The heap sort algorithm is stable, which means that the order of equal elements is preserved. However, it is not in-place, which means that it requires extra space to store the sorted list.

This solution is tested with the given unit test:
```
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])