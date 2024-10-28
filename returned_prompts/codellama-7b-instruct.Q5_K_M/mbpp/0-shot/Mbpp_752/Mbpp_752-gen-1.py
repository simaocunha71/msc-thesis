
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 == 0:
        return jacobsthal_num(n//2)
    else:
        return 2*jacobsthal_num(n//2) + 1
    
    # or
    
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return 2*jacobsthal_num(n//2) + 1
    
    # or
    
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 == 0:
        return jacobsthal_num(n//2)
    else:
        return jacobsthal_num(n//2) + 1
    
    # or
    
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return jacobsthal_num(n//2) + 1
    
    # or
    
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 == 0:
        return jacobsthal_num(n//2)
    else:
        return jacobsthal_num(n//2) + 1
    
    # or
    
def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 