def next_smallest_palindrome(n: int) -> int:
    if n <= 11:
        return n + 1
    n_str = str(n)
    length = len(n_str)
    mid = length // 2
    left_half = n_str[:mid]
    right_half = n_str[mid:] if length % 2 == 0 else n_str[mid+1:]
    right_half = right_half[::-1]
    if length % 2 == 0:
        next_palindrome = int(left_half + right_half)
    else:
        next_palindrome = int(left_half + n_str[mid] + right_half)
    return next_palindrome if next_palindrome <= n else next_smallest_palindrome(next_palindrome)