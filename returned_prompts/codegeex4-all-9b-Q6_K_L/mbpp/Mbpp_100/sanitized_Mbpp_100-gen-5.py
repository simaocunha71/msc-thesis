def next_smallest_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)
    if n_len == 1:
        return n + 1

    # Generate the next palindrome
    half = n_str[:n_len // 2]
    next_half = str(int(half) + 1)
    if n_len % 2 == 0:
        next_palindrome = next_half + next_half[::-1]
    else:
        next_palindrome = next_half + next_half[-2::-1]

    return int(next_palindrome)