    def is_palindrome(arr):
        return arr == arr[::-1]

    def count_changes(arr):
        if is_palindrome(arr):
            return 0
        else:
            min_changes = float('inf')
            for i in range(len(arr)):
                arr_copy = arr.copy()
                arr_copy[i] = arr[0]
                min_changes = min(min_changes, count_changes(arr_copy) + 1)
            return min_changes

    return count_changes(arr)  # call the function with the input array


