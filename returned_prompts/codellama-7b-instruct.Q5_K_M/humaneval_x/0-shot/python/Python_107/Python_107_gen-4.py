
def even_odd_palindrome(n):
    even_cnt = 0
    odd_cnt = 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
    return (even_cnt, odd_cnt)

