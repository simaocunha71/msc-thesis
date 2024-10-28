def heap_sort(lst):
    heapify(lst)
    end = len(lst) - 1
    while end > 0:
        lst[end], lst[0] = lst[0], lst[end]
        end -= 1
        sift_down(lst, 0, end)
    return lst
def sift_down(lst, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if lst[swap] < lst[child]:
            swap = child
        if child + 1 <= end and lst[swap] < lst[child + 1]:
            swap = child + 1
        if swap != root:
            lst[root], lst[swap] = lst[swap], lst[root]
            root = swap
        else:
            return