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
The shell_sort function starts by dividing the length of the array by 2 to get the initial gap size. 
Then it starts a while loop that continues until the gap size is 0. Inside the while loop, it starts a for loop that 
iterates through the array starting from the gap size to the length of the array. Inside the for loop, it swaps the 
elements if the current element is smaller than the previous element. This is done by using a temp variable to store 
the current element and then setting the current element to the previous element and the previous element to the temp 
variable. Finally, it halves the gap size and continues the loop until the gap size is 0.
"""

# Time complexity: O(n^2) in the worst case, but it performs very well on large lists and can be faster in practice.
# Space complexity: O(1) as it is an in-place sorting algorithm.
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
2. Bubble Sort
<jupyter_code>
