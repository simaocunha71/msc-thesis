
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)

print(even_odd_palindrome(3))  # Expected output: (1, 2)
print(even_odd_palindrome(12))  # Expected output: (4, 6)

This solution works by iterating through the numbers from 1 to n. For each number, it checks whether it's a palindrome using the helper function is_palindrome(). If the number is a palindrome, it checks whether it's even or odd and increments the corresponding count. Finally, it returns a tuple of the counts of even and odd palindromes.

This solution runs in O(n) time complexity because it performs a single pass through the range of numbers from 1 to n. It also has O(n) space complexity because it stores the counts of even and odd palindromes.

Please note that the constraints of the problem (1 <= n <= 10^3) ensure that this solution will execute within reasonable time limits.
