def heap_sort(my_list):
    def sift_down(start, end):
        root = start
        while 2*root + 1 <= end:
            child = 2*root + 1
            if child < end and my_list[child] < my_list[child + 1]:
                child += 1
            if my_list[root] < my_list[child]:
                my_list[root], my_list[child] = my_list[child], my_list[root]
                root = child
            else:
                break

    def heapify(my_list):
        n = len(my_list)
        for i in range(n//2-1, -1, -1):
            sift_down(i, n-1)

    heapify(my_list)
    for i in range(len(my_list)-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        sift_down(0, i-1)
    return my_list

