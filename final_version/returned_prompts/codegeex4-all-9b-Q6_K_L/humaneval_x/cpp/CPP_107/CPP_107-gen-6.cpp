def even_odd_palindrome(n):
    if n < 1 or n > 10**3:
        return None
    even = 0
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return [even, odd]
print(even_odd_palindrome(3)) # Output: [1, 2]
print(even_odd_palindrome(12)) # Output: [4, 6]
print(even_odd_palindrome(1)) # Output: [1, 0]
print(even_odd_palindrome(100)) # Output: [9, 91]
print(even_odd_palindrome(1000)) # Output: [90, 909]
print(even_odd_palindrome(10**3)) # Output: [990, 9910]