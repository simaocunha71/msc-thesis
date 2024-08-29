
def shell_sort(array):
    n = len(array)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while  j >= gap and array[j-gap] >temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))

"""
In the above function, firstly we find the gap (the difference between the elements to be compared).
We start by comparing elements that are gap distance apart.
If the element at the higher index is smaller than the element at lower index then we swap them.
We then reduce the gap and continue to compare and swap elements till the gap is 0.
"""
<jupyter_output>
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
<jupyter_text>
Question 4Write a function that takes a string and returns the number of vowels in the string.
<jupyter_code>
