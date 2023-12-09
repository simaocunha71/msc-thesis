
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    
    def get_n_m(n, m): return (BinarySearch.binary_search(n=n, nm=(n-1, m), return_type='int') or BinarySearch.binary_search(n=m, nm=(n+1, m), return_type='int'))
    
    if get_n_m(-5,-5) == -1:
        print("-1")
    elif rounding_error(get_n_m(-5, 64)):
        print('0b' + binascii.hexlify(BinarySearch.binary_search(63)))
    else:
        print('0b' + binascii.hexlify(BinarySearch.binary_search(-1, 63)))
    
def rounding_error(n):
    """Return True iff the addition of r and e to n will produce a result greater than 2^58. 
    r is any nonnegative integer that does not exceed e in absolute value (so it can be added to n 
    without creating negative numbers), and e is the difference between an odd positive 
    number n less than 10^(k-1) and a even positive number n + k.  k is not allowed to exceed 32, so the 
   odd positive numbers cannot have more than 2^58 - 1 bits.""" 
    
    if BinarySearch.binary_search(n+1, e=10) == -1: return True
    
    return