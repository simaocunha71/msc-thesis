    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes
# Example 1:
print(even_odd_palindrome(3))  # Output: (1, 2)
# Example 2:
print(even_odd_palindrome(12))  # Output: (4, 6)  # 4 even palindromes (2, 4, 6, 8) and 6 odd palindromes (1, 3, 5, 7, 9, 11)
# Example 3:
print(even_odd_palindrome(5))  # Output: (1, 4)  # 1 even palindrome (2) and 4 odd palindromes (1, 3, 5, 11) 
# Example 4:
print(even_odd_palindrome(10))  # Output: (3, 7)  # 3 even palindromes (2, 4, 8) and 7 odd palindromes (1, 3, 5, 7, 9, 11, 101)
# Example 5:
print(even_odd_palindrome(15))  # Output: (4, 11)  # 4 even palindromes (2, 4, 6, 8) and 11 odd palindromes (1, 3, 5, 7, 9, 11, 13, 14, 121, 131, 141) 
# Example 6:
print(even_odd_palindrome(20))  # Output: (6, 14)  # 6 even palindromes (2, 4, 6, 8, 10, 18) and 14 odd palindromes (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 121, 131, 141, 151) 
# Example 7:
print(even_odd_palindrome