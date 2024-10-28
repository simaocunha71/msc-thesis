    def is_palindromic(arr):
        return arr == arr[::-1]

    def smallest_change_helper(arr, start, end):
        if start > end:
            return 0

        if arr[start] == arr[end]:
            return smallest_change_helper(arr, start + 1, end - 1)

        return smallest_change_helper(arr, start + 1, end) + 1

    return smallest_change_helper(arr, 0, len(arr) - 1)



