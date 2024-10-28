def next_smallest_palindrome(n):
    '''
    Find the next smallest palindrome of a specified integer
    '''
    n += 1
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1