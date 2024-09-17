```
def heap_sort(lst):
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
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
```


Heap sort is a comparison-based sorting technique based on a Binary Heap data structure. It is similar to merge sort. It has a time complexity of O(n log n). The basic idea is to build a heap and then remove the largest item, heapify the remaining items, and repeat this process until the heap is empty.

This function starts by building a max heap from the input list. It does this by iterating through the list from the last non-leaf node to the root, and heapifying each node. This ensures that the largest item is at the root of the heap.

Then it repeatedly removes the largest item (which is at the root) and heapifies the remaining items. This ensures that the largest item is at the end of the list. The process is repeated until the heap is empty, at which point the list is sorted.

The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` ensures that the function correctly sorts the input list.