def next_smallest_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    s = str(n)
    if s == s[::-1]:
        return int(s) + 1
    else:
        return int(s[1:] + s[:-1])
































