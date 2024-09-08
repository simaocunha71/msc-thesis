
def check_min_heap(arr):
    n = len(arr)

    for i in range(int(n/2)-1):
        if arr[i] > arr[2*i+1]:
            return False
        if 2*i+2 < n:
            if arr[i] > arr[2*i+2]:
                return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6]))

# Time Complexity: O(n)
# Space Complexity: O(1)
<jupyter_output>
True
<jupyter_text>
Problem 2: Convert an array to min heapGiven an array, the task is to convert the array into a min heap.  The conversion should be in place, i.e., the initial array should be modified.
<jupyter_code>
