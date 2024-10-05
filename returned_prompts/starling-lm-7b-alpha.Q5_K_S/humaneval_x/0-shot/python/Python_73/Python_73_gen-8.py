    # O(n) solution
    def smallest_change(arr):
        odd = 0
        even = 0
        for i in range(len(arr)):
            if i == len(arr) - i - 1:
                continue
            if arr[i] != arr[len(arr) - i - 1]:
                if arr[i] == arr[len(arr) - i - 1] + 1:
                    odd += 1
                elif arr[i] + 1 == arr[len(arr) - i - 1]:
                    even += 1
                else:
                    odd += 1
                    even += 1
        return even // 2 + odd

    return smallest_change(arr)



# O(n^2) solution
def smallest_change_slow(arr):
    def is_palindrome(arr):
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - i - 1]:
                return False
        return True

    def smallest_change_helper(arr, i, j):
        if i >= j:
            return 0
        if arr[i] != arr[j]:
            return 1 + min(smallest_change_helper(arr, i + 1, j),
                           smallest_change_helper(arr, i, j - 1))
        return smallest_change_helper(arr, i + 1, j - 1)

    return smallest_change_helper(arr, 0, len(arr) - 1)


# O(n^2) solution
def smallest_change_slow(arr):
    def is_palindrome(arr):
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - i - 1]:
                return False
        return True

    def smallest_change_helper(arr, i, j):
        if i >= j:
            return 0
        if arr[i] != arr[j]:
            return 1 + min(smallest_change_helper(arr, i + 