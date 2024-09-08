def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2
    return arr

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))

"""
Explanation:
Shell sort is an algorithm that improves on the insertion sort by breaking the original list into smaller sublists.
The idea of shell sort is to allow the exchange of items that are far apart. In other words, it allows the interchanging of elements that are in different subarrays.
The gap is initially set to length of the array divided by 2. The elements at the gapth position are compared. If the item in the gapth position is greater than the item in the 0th position, they are swapped.
The value of gap is halved in the next iteration. The process continues until the gap is 1.
"""
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
**Question 3**
<jupyter_code>
