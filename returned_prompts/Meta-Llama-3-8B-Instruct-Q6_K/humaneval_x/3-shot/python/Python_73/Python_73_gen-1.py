    def is_palindromic(arr):
        return arr == arr[::-1]

    def min_changes(arr):
        if is_palindromic(arr):
            return 0

        # Find the center of the array
        center = len(arr) // 2

        # If the array is odd, the center is the middle element
        if len(arr) % 2 != 0:
            center = center

        # If the array is even, the center is the two middle elements
        else:
            center = center - 1

        # Find the number of changes needed to make the left half a palindrome
        left_changes = sum(1 for i in range(center) if arr[i] != arr[-i - 1])

        # Find the number of changes needed to make the right half a palindrome
        right_changes = sum(1 for i in range(center + 1, len(arr)) if arr[i] != arr[center - i])

        # The total number of changes is the sum of the left and right changes
        return left_changes + right_changes

    return min_changes(arr)  # Call the helper function with the input array
# end of solution
# end of 