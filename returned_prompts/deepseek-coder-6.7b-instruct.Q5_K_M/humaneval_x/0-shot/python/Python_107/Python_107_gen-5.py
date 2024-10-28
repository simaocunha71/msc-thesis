
    def even_odd_palindrome(n):
        def is_palindrome(x):
            return str(x) == str(x)[::-1]

        even_count = sum(is_palindrome(i) and i % 2 == 0 for i in range(1, n + 1))
        odd_count = sum(is_palindrome(i) and i % 2 != 0 for i in range(1, n + 1))

        return (even_count, odd_count)

    print(even_odd_palindrome(3))  # Output: (1, 2)
    print(even_odd_palindrome(12))  # Output: (4, 6)

Explanation:

In this solution, we first define a helper function is_palindrome that checks if a number is a palindrome by comparing the string representation of the number with its reverse.

Then we count the number of even and odd palindromes in the range of 1 to n. We do this by iterating over the range and using the is_palindrome function to check if a number is a palindrome. We also use the modulus operator to check if a number is even or odd.

Finally, we return a tuple of the count of even and odd palindromes.

The time complexity is O(n) and the space complexity is O(1), where n is the input number.

This solution works for the given constraints and is efficient for small to medium sized inputs.
"""

def even_odd_palindrome(n):
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    even_count = sum(is_palindrome(i) and i % 2 == 0 for i in range(1, n + 1))
    odd_count = sum(is_palindrome(i) and i % 2 != 0 for i in range(1, n + 1))

    return (even_count, odd_count)

print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome