def even_odd_palindrome(n):
    evens = sum(1 for i in range(1, n+1) if str(i) == str(i)[::-1] and i % 2 == 0)
    odds = sum(1 for i in range(1, n+1) if str(i) == str(i)[::-1] and i % 2 == 1)
    return (evens, odds)

print(even_odd_palindrome(3))  # (1, 2)
print(even_odd_palindrome(12))  # (4, 6)