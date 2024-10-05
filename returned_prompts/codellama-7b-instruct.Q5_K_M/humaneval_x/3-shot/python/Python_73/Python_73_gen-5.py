    def reverse(l):
        return l[::-1]

    def is_palindrome(l):
        return l == reverse(l)

    arr = reverse(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr[i - 1]:
            count += 1

    return count


