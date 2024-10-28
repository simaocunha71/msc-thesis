
def even_odd_palindrome(n):
    """
    :type n: int
    :rtype: tuple
    """
    even = 0
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
        elif str(i) == str(i)[::-1] and i % 2 == 1:
            odd += 1
    return (even, odd)
