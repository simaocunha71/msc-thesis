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