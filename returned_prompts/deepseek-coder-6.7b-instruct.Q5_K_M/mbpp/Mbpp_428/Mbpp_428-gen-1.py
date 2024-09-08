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
        gap //= 2
    return arr

print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))

"""
This function sorts an array by taking a 'gap' value which is initially half of the length of the array. It then uses a for loop to iterate over the array starting from the gap value. Inside the for loop, a temporary variable is used to store the current element. Then, a while loop is used to compare the current element with the elements at a distance of the gap. If the current element is smaller, the elements at a distance of the gap are shifted to the right. This process is repeated until the correct position for the current element is found. The gap value is then halved and the process is repeated until the gap value is 0. Finally, the sorted array is returned.
"""

"""
Time complexity:
The time complexity of Shell Sort is O(n^2) in the worst case scenario. It can be O(n^2) or less depending on the gap sequence.

Space complexity:
The space complexity of Shell Sort is O(1).
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Bubble Sort
<jupyter_code>
