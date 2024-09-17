def next_smallest_palindrome(x):
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]
 
    if not is_palindrome(x + 1):
        return x + 1
 
    for i in range(x + 1, 100000):
        if is_palindrome(i):
            return i