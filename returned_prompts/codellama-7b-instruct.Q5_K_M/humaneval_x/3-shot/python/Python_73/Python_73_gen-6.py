    left, right = 0, len(arr) - 1
    palindrome_count = 0
    while left < right:
        if arr[left] != arr[right]:
            arr[left] = arr[right]
            palindrome_count += 1
        left += 1
        right -= 1

    return palindrome_count


