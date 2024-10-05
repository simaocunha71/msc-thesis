    def is_palindromic(arr):
        """
        Return True if the array is palindromic, False otherwise.
        """
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - i - 1]:
                return False

        return True

    def is_palindromic_subarray(arr, start, end):
        """
        Return True if the subarray arr[start:end] is palindromic, False otherwise.
        """
        for i in range(start, end):
            if arr[i] != arr[end - i + start]:
                return False

        return True

    def smallest_change_subarray(arr, start, end):
        """
        Find the smallest number of changes to make the subarray arr[start:end] palindromic.
        """
        min_changes = float('inf')

        for i in range(start, end):
            if is_palindromic_subarray(arr, start, i) or is_palindromic_subarray(arr, i, end):
                min_changes = min(min_changes, 1)

        return min_changes

    min_changes = float('inf')

    for i in range(len(arr)):
        min_changes = min(min_changes, smallest_change_subarray(arr, i, len(arr)))

    return min_changes


