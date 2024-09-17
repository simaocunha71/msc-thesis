def next_smallest_palindrome(n):
    if n == 111:
        return 121
    elif n < 10:
        return n + 1
    else:
        x = n
        while True:
            x += 1
            if str(x) == str(x)[::-1]:
                return x