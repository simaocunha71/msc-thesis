
def heap_sort(lst):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]

print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

#Answer:
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
