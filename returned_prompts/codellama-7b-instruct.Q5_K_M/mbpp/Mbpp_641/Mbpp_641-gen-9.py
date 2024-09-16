def is_nonagonal(n):
    return n*(3*n-1)//2 == 2*n*n

def find_nonagonal(n):
    if is_nonagonal(n):
        return n
    else:
        return find_nonagonal(n+1)

print(find_nonagonal(10))
