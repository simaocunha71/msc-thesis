    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes
# This function works by iterating over all numbers from 1 to n, converting each number to a string and checking if it's a palindrome.
# If it is, it checks if the number is even or odd, and increments the corresponding counter. Finally, it returns the counts of even and odd palindromes.
# Time complexity: O(n) where n is the input number.
# Space complexity: O(1) as it only uses a constant amount of space.