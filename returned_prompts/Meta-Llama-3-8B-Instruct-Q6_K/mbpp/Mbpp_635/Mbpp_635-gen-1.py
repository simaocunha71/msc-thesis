```
def heap_sort(lst):
    if len(lst) <= 1:
        return lst
    heap = []
    for num in lst:
        heapq.heappush(heap, num)
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list
```
This function uses the heapq module to sort the list. It first builds a heap from the input list, then repeatedly removes the smallest item from the heap and adds it to the sorted list. The result is a sorted list in ascending order. The unit test provided ensures that the function works correctly.