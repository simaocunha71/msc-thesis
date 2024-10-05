
def smallest_change(arr):
    # Write your code here
    if not arr:
        return 0
    arr_len = len(arr)
    # find the middle index
    mid = arr_len // 2
    # find the palindrome
    palindrome = [None] * arr_len
    # fill the palindrome with the middle
    for i in range(arr_len):
        palindrome[i] = arr[i]
    # fill the rest of the palindrome
    for i in range(arr_len):
        palindrome[arr_len - i - 1] = arr[i]

    # find the indices of the non-palindrome elements
    non_palindrome_indices = []
    for i in range(arr_len):
        if arr[i] != palindrome[i]:
            non_palindrome_indices.append(i)
    # return the number of indices
    return len(non_palindrome_indices)
