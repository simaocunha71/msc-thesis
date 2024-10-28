```
def heap_sort(lst):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(lst)
    for i in range(n, -1, -1):
        heapify(lst, n, i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
```


Explanation:
This is a Python solution for the problem of sorting a list using the heap sort algorithm. 

The function `heap_sort` first defines a helper function `heapify` which is used to build a max heap. It does this by iterating over the list, and for each element, it checks if the left or right child is larger, and if so, it swaps the element with the larger child and recursively calls `heapify` on the affected subtree.

After building the max heap, the function then repeatedly removes the root element (which is the largest element) and places it at the end of the list. It then calls `heapify` on the reduced heap to maintain the heap property.

Finally, the function returns the sorted list. The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` confirms that the function works correctly. 