
def even_odd_palindrome(n):
    num_of_even_palindrome = 0
    num_of_odd_palindrome = 0
    for i in range(1, n+1):
        if is_palindrome(i) and i % 2 == 0:
            num_of_even_palindrome += 1
        elif is_palindrome(i) and i % 2 == 1:
            num_of_odd_palindrome += 1
    return (num_of_even_palindrome, num_of_odd_palindrome)

def is_palindrome(n):
    return str(n) == str(n)[::-1]
