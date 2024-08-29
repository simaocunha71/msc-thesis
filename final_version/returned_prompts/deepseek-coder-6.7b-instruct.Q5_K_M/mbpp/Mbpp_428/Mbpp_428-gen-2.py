def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))

"""
The time complexity of the shell sort is dependent on the gap sequence. The worst-case time complexity of shell sort is O(n^2), which occurs when the gap sequence is 1. The best case time complexity of shell sort is O(n^1.5) for a gap sequence of 1, 4, 13, 40, 121, ... etc.
"""
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
Quick Sort Algorithm
<jupyter_code>
