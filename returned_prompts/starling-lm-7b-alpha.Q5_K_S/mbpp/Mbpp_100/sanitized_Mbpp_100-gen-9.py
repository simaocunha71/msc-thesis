def next_smallest_palindrome(n):
    if not isinstance(n, int):
        raise TypeError("Input is not an integer")
    if n < 10:
        return n + 1
    s = str(n)
    for i in range(len(s)):
        if s[i] != '9':
            break
    if i == len(s) - 1:
        return str(int(s[:i]) + 1 + '0' * (len(s) - i - 1))
    else:
        return str(int(s[:i] + chr(ord(s[i]) + 1) + '9' * (len(s) - i - 1)))