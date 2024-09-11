Here's one way to implement shell sort in Python:

```python
def shell_sort(nums):
    # Initialize the gap
    gap = len(nums) // 2

    # Loop through the array
    while gap > 0:
        # Loop through the array
        for i in range(gap, len(nums)):
            # Save the current element
            temp = nums[i]

            # Shift all elements that are greater than temp one position to the right
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap

            # Place temp in its correct location
            nums[j] = temp

        # Reduce the gap
        gap //= 2

    return nums
```
This function takes an array of numbers and sorts it using the shell sort algorithm. The shell sort algorithm works by first sorting subarrays of larger and larger size, and then merging them back together. In this implementation, the gap variable is used to determine the size of the subarrays. The function initializes the gap to half the length of the array, and then repeatedly reduces it by dividing it by 2 until it becomes 0. Within each iteration, the function loops through the array and compares each element with its neighbors. If an element is greater than its neighbor, it is swapped with the neighbor. This process is repeated until all elements are in their correct positions. Finally, the sorted array is returned.
```python
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```
This assertion checks if the shell_sort function correctly sorts the given array [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]. The expected output is [2, 3, 4, 5, 12