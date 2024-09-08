def heap_sort(lst):
    heapify(lst)
    end = len(lst) - 1
    while end > 0:
        lst[end], lst[0] = lst[0], lst[end]
        end -= 1
        sift_down(lst, 0, end)
    return lst

def heapify(lst):
    start = len(lst) // 2 - 1
    while start >= 0:
        sift_down(lst, start, len(lst) - 1)
        start -= 1

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

# Test
print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# This code is contributed by @akash1412000
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<jupyter_text>
Heap Sort ExplanationThis heap sort algorithm works by transforming the input list into a heap, then continually extracting the largest element, placing it at the end of the list, and sifting down the new root to restore the heap property. The time complexity of heap sort is O(n log n), and it's not suitable for small lists.
<jupyter_code>

<jupyter_