
    def even_odd_palindrome(n):
        def is_palindrome(num):
            return str(num) == str(num)[::-1]

        even_count = sum(is_palindrome(i) and i % 2 == 0 for i in range(1, n + 1))
        odd_count = sum(is_palindrome(i) and i % 2 == 1 for i in range(1, n + 1))

        return (even_count, odd_count)

    print(even_odd_palindrome(3))  # (1, 2)
    print(even_odd_palindrome(12))  # (4, 6)

Explanation:

This solution defines a helper function is_palindrome that checks if a given number is a palindrome. It then counts the number of even and odd palindromes within the range using a generator expression and sum function. The counts are then returned in a tuple.

The helper function is_palindrome converts a number to a string and checks if it is equal to its reverse (which would be a palindrome). The number is also checked for even or oddness. The sum function is used to count the number of palindromes that meet these conditions.

The function is then tested with the examples provided in the question.

The time complexity of this solution is O(n), as it checks all numbers up to n to see if they are palindromes. The space complexity is O(1), as it only uses a constant amount of space to store the counts and the number n.

The solution meets the time and space complexity requirements of the problem.

Note: The function assumes that by "odd integer palindrome" you mean palindromes with an odd number of digits, which is the usual definition in mathematics. If by "odd integer palindrome" you mean palindromes that contain an odd number of odd digits, the function would need to be modified.

Note: The function uses Python's built-in sum function and generator expressions, which are both efficient and idiomatic ways to solve the problem.

Note: The function uses Python's built-in sum function and generator expressions, which are both efficient and idi