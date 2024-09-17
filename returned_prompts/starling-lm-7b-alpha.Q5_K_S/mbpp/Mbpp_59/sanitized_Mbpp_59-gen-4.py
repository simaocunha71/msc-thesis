def is_octagonal(n):
    if n==1:
        return True
    elif n%2==1:
        return is_octagonal(n-1) and is_octagonal(n-3)
    elif n%8==0:
        return is_octagonal(n/8)
    else:
        return False