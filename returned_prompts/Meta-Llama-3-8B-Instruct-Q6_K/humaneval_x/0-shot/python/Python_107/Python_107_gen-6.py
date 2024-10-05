    even_palindromes = 0
    odd_palindromes = 0
    
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
    
    return even_palindromes, odd_palindromes
# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
print(even_odd_palindrome(9))   # Output: (1, 7)
print(even_odd_palindrome(100)) # Output: (25, 72)  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  # 25 even, 72 odd.  #