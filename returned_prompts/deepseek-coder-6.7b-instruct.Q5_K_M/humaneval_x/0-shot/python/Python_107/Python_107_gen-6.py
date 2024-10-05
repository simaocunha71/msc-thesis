
def even_odd_palindrome(n):
    even_palindromes = 0
    odd_palindromes = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
    return (even_palindromes, odd_palindromes)

# Test cases
print(even_odd_palindrome(3))  # (1, 2)
print(even_odd_palindrome(12))  # (4, 6)

This solution works by iterating from 1 to n and checking if the number is a palindrome by comparing it to its reverse. If it is, it checks if the number is even or odd and increases the appropriate counter. Finally, it returns the counts of even and odd palindromes as a tuple.

It is important to note that this solution has a time complexity of O(n), where n is the input number. This is because it needs to iterate through every number up to n to check if it is a palindrome and to count the number of even and odd palindromes.
