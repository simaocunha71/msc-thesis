    def get_palindrome(arr):
        result = []
        left = 0
        right = len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                result.append(max(arr[left], arr[right]))
            left += 1
            right -= 1
        result += arr[left:right+1]
        return result

    def get_num_changes(arr, palindrome):
        count = 0
        for i in range(len(arr)):
            if arr[i] != palindrome[i]:
                count += 1
        return count

    palindrome = get_palindrome(arr)
    return get_num_changes(arr, palindrome)


