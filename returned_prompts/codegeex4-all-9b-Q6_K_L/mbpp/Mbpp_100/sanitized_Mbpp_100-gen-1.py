def next_smallest_palindrome(n):
    if n < 10:
        return n + 1
    str_n = str(n)
    length = len(str_n)
    if length == 1:
        return n + 1
    mid = length // 2
    left = str_n[:mid]
    if length % 2 == 0:
        right = str_n[mid:]
    else:
        right = str_n[mid+1:]
    right_reversed = right[::-1]
    if right_reversed == right:
        left = str(int(left) - 1)
        right = str(int(left[::-1]))
    else:
        right = right_reversed
    if length % 2 == 0:
        return int(left + right)
    else:
        return int(left + right + left[-1])