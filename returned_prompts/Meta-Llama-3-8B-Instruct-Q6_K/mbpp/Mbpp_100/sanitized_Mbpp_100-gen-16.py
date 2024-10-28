def next_smallest_palindrome(n):
    if n % 11 == 0:
        return n + 1
    else:
        return int(str(n + 1)[::-1] + str(n + 1))  # convert int to string, reverse it, then concatenate with the original int converted to string