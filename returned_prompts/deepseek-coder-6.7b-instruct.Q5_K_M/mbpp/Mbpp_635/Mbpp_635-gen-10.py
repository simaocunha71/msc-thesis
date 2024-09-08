def heap_sort(arr):
    # Convert the array into a max heap
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # Sort the array
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr

def sift_down(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child = child + 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
The above solution sorts the array by first transforming it into a max heap, then continuously swapping the root of the heap with the last item of the heap followed by sifting down the new root to the appropriate position.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.Example:Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].
<jupyter_code>
