```
def heap_sort(lst):
    if len(lst) > 0:
        heap = lst[:]
        heapify(heap, len(heap))
        sorted_list = []
        while len(heap) > 0:
            sorted_list.append(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            heapify(heap, len(heap))
        return sorted_list[::-1]
    return []

def heapify(lst, n):
    for i in range(n//2-1, -1, -1):
        sift_down(lst, i, n)

def sift_down(lst, start, end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:
            return
        if child + 1 <= end and lst[child] < lst[child+1]:
            child += 1
        if lst[root] >= lst[child]:
            return
        lst[root], lst[child] = lst[child], lst[root]
        root = child
```

The function heap_sort takes a list as input and returns the sorted list. It first checks if the list is not empty. If it's not empty, it creates a heap from the list and then repeatedly removes the root element from the heap and places it at the end of the sorted list. The heapify function is used to maintain the heap property after each removal. The sift_down function is a helper function used by heapify to move down the elements of the heap. 

The time complexity of this solution is O(n log n) because heapify operation takes O(log n) time and it's performed n times. The space complexity is O(1) because it only uses a constant amount of space to store the heap and the sorted list. 

The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` checks if the function correctly sorts a list in ascending order. 

Please note that the problem is asking to sort the list in ascending order, not descending order. The `heap_sort` function returns the sorted list in ascending order. If you want to sort the list in descending order, you can modify the function to return the sorted list in reverse order. 

Also, the problem is asking to use a