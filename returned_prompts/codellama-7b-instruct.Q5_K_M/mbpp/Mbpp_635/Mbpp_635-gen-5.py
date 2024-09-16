def heap_sort(my_list):
    def max_heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, n, largest)
    def build_max_heap(arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            max_heapify(arr, n, i)
    def heap_sort(arr):
        build_max_heap(arr)
        n = len(arr)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            max_heapify(arr, i, 0)
        return arr
    return heap_sort(my_list)
