def heap_sort(lst):
    heap = []
    for num in lst:
        heap.append(num)
        i = len(heap) - 1
        while i > 0 and heap[i] < heap[(i-1)//2]:
            heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
            i = (i-1)//2
    for i in range(len(heap)-1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        j = 0
        while 2*j+1 < i:
            smaller = 2*j+1
            if 2*j+2 < i and heap[2*j+2] < heap[2*j+1]:
                smaller = 2*j+2
            if heap[j] < heap[smaller]:
                break
            heap[j], heap[smaller] = heap[smaller], heap[j]
            j = smaller
    return heap