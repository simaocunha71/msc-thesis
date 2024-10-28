
    def even_odd_palindrome(n):
        def is_palindrome(x):
            return str(x) == str(x)[::-1]

        even_count = sum(is_palindrome(i) and i % 2 == 0 for i in range(1, n+1))
        odd_count = sum(is_palindrome(i) and i % 2 == 1 for i in range(1, n+1))

        return (even_count, odd_count)

    print(even_odd_palindrome(3))  # Output: (1, 2)
    print(even_odd_palindrome(12))  # Output: (4, 6)

Explanation:

This program counts the number of even and odd palindromes in the range from 1 to n inclusive. A helper function is_palindrome(x) checks if the integer x is a palindrome by comparing the string representation of x with its reverse. The program then counts the number of palindromes that are even and odd by summing the results of the generator expressions.

The generator expressions use a for loop to iterate over the range from 1 to n inclusive, and include the condition for each number to be a palindrome and to be even or odd. The results of these conditions are True or False, which are converted to 1 (True) or 0 (False) by the sum function.

Finally, the program returns a tuple with the counts of even and odd palindromes.

The time complexity of this program is O(n) because it needs to iterate over the range of numbers from 1 to n. The space complexity is O(1) because it uses a constant amount of space to store the counts and the number n.

This program satisfies the constraints of the problem because the input n is in the range [1, 10^3] and the output is a tuple with two elements, each of which is a count of palindromes.

The program should work correctly for all valid inputs in the given range. However, it may be slow for large inputs due to the time complexity.
"""

# Test cases
print(even_odd_palindrome(3))  # Output