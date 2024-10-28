
def even_odd_palindrome(n):
    # Write your code here
    even = 0
    odd = 0
    for i in range(1, n + 1):
        if is_even_pal(i):
            even += 1
        else:
            odd += 1
    return (even, odd)

def is_even_pal(x):
    return str(x) == str(x)[::-1]
