    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    e_count = 0
    o_count = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                e_count += 1
            else:
                o_count += 1
    return e_count, o_count


