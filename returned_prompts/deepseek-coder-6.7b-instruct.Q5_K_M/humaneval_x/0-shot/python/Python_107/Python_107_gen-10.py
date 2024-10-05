
    def even_odd_palindrome(n):
        even, odd = 0, 0
        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return (even, odd)

    print(even_odd_palindrome(3))  # Output: (1, 2)
    print(even_odd_palindrome(12))  # Output: (4, 6)

Explanation:

    The function `even_odd_palindrome` takes an integer `n` as input. It initializes two variables, `even` and `odd`, to 0 to keep track of the number of even and odd palindromes.

    Then it loops over all the numbers from 1 to `n` (inclusive). For each number, it checks if the number is a palindrome by comparing the string representation of the number with its reverse. If they are equal, it means the number is a palindrome.

    If the number is a palindrome, it then checks if the number is even or odd by checking if the remainder of the number when divided by 2 is 0 (`i % 2 == 0`). If it is, it increments the `even` variable; if not, it increments the `odd` variable.

    Finally, it returns a tuple of the counts of even and odd palindromes.

    The time complexity of this solution is O(n), where n is the input number. The space complexity is O(1), as it only uses a constant amount of space to store the counts of even and odd palindromes.

    The function can be tested by calling it with various inputs.
    """

# ==============
# 
# ==============
# 
# 
# ==============
# 
# 
# ==============
# 
# 
# ==============
# 
# 
# ==============
# 
# 
# ==============
# 
# 
# =