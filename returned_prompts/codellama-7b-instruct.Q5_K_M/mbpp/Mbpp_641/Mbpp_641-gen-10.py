def is_nonagonal(n):
    return ((n-1)**2 + (n-1))**2 == n

def find_nth_nonagonal(n):
    i = 1
    while i < n:
        i += 1
        if is_nonagonal(i):
            n -= 1
    return i

print(find_nth_nonagonal(10)) # 325
print(is_nonagonal(325)) # True
