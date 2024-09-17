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
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)
    return lst
```


This function implements the heap sort algorithm. It first builds a max heap from the input list, then repeatedly extracts the maximum element from the heap and places it at the end of the list, until the heap is empty. The list is then returned as the sorted output.

The `heapify` function is used to maintain the heap property. It takes a list `lst`, its length `n`, and an index `i` as input. It finds the largest element among the current node and its children, and swaps the two if necessary. The function is then called recursively on the affected sub-tree.

The main function first builds the heap by calling `heapify` on each non-leaf node in reverse order. Then it repeatedly extracts the maximum element from the heap and places it at the end of the list, until the heap is empty. The list is then returned as the sorted output. 





The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` ensures that the function correctly sorts the input list in ascending order.