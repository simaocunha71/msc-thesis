def next_smallest_palindrome(n: int) -> int:
    s = str(n)
    if s == s[::-1]:
        return int(s) + 1
    else:
        l = len(s)
        for i in range(l):
            if s[i] != s[l-i-1]:
                break
        left = s[:i]
        right = s[i+1:l]
        if i == 0:
            return int(right + left + '1')
        elif i == l-1:
            return int(left + right + '1')
        else:
            return int(left + right + '1')