def is_num_decagonal(n):
    return True if (n>=1) and (n % 2 == 0) and (n % 9 == 0) else False

def nth_decagonal(n):
    return (n*(n+1))//2 + (n*(n+1)//19)


"""
Tests
"""
assert is_num_decagonal(3) == True
assert nth_decagonal(3) == 27

