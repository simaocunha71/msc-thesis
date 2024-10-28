def next_smallest_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return int(n) + 1
    else:
        n = n[::-1]
        for i in range(len(n)):
            if n[i] != n[-1-i]:
                break
        n = n[:-1-i] + str(int(n[-1-i]) + 1) + n[i+1::]
        return int(n)