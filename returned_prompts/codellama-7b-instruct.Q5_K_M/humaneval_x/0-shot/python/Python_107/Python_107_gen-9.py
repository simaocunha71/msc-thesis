
def even_odd_palindrome(n):
    count_even, count_odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            count_even += 1
        elif str(i) == str(i)[::-1] and i % 2 == 1:
            count_odd += 1
    return (count_even, count_odd)
