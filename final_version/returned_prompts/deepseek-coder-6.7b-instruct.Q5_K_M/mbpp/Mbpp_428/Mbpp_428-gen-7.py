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
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
**Question 4**
<jupyter_code>
