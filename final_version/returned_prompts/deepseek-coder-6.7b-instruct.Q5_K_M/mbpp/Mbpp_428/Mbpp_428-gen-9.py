def shell_sort(arr):
    n = len(arr)
    gap = n//2

    # Start with a big gap, then reduce the gap
    while gap > 0:

        # Do a gapped insertion sort for this gap size.The first gap elements a[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap sorted
        for i in range(gap,n):

            # add a[i] to the elements that have been gap sorted save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2

    return arr

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
Problem 2
<jupyter_code>
