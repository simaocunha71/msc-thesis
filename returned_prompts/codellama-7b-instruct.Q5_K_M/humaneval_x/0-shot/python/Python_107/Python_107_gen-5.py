
def even_odd_palindrome(n):
    def is_even_odd_palindrome(x):
        s = str(x)
        return len(s) == len(set(s)) and s == s[::-1]

    count_even = 0
    count_odd = 0
    for i in range(1, n):
        if is_even_odd_palindrome(i):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
