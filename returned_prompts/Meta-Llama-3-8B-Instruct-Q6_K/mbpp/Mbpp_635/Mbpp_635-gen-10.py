```
def heap_sort(lst):
    for i in range(len(lst)//2-1, -1, -1):
        heapify(lst, i, len(lst))
    for i in range(len(lst)-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
    return lst

def heapify(lst, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[i] < lst[left]:
        largest = left
    if right < n and lst[largest] < lst[right]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, largest, n)
```
The heap sort algorithm sorts the list by first transforming it into a heap, and then repeatedly removing the largest element and placing it at the end of the list. 

The function `heap_sort` takes a list as input, and returns the sorted list. 

The function `heapify` is a helper function that is used to maintain the heap property. 

The heap property is that the parent node is either greater than or equal to its children. 

The `heapify` function starts at the root node, and recursively heapifies the left and right subtrees until the heap property is satisfied. 

The `heap_sort` function first builds the heap, and then repeatedly removes the largest element and places it at the end of the list. 

The `heap_sort` function returns the sorted list. 





The unit test `assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` ensures that the `heap_sort` function correctly sorts the list in ascending order.