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
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
```



The heap sort function sorts the given list in ascending order. It uses the heapify function to maintain the heap property. The heapify function is called for each non-leaf node in reverse order, and then the largest element is moved to the end of the heap. This process is repeated until the heap is empty, resulting in a sorted list. The time complexity of heap sort is O(n log n) in the worst case.