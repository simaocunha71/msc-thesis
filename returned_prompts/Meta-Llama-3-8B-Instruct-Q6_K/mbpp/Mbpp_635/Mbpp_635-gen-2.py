```
def heap_sort(lst):
    def heapify(lst, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and lst[i] < lst[l]:
            largest = l
        if r < n and lst[largest] < lst[r]:
            largest = r
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest)
    n = len(lst)
    for i in range(n, -1, -1):
        heapify(lst, n, i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
```


The code defines a heap sort function that sorts a given list. It uses the heapify function to build a max heap and then repeatedly extracts the maximum element and places it at the end of the list, until the heap is empty. The heapify function rearranges the list to satisfy the heap property, where the parent node is greater than or equal to its child nodes. The function returns the sorted list. The unit test provided ensures that the function works correctly for the given list.