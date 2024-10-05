    def is_palindrome(s):
        return s == s[::-1]

    def count_palindrome(n):
        count = 0
        for i in range(1, n + 1):
            if is_palindrome(str(i)):
                count += 1
        return count

    even_count = count_palindrome(n)
    odd_count = count_palindrome(n) - sum(is_palindrome(str(i)) and i % 2 != 0 for i in range(1, n + 1))

    return (even_count, odd_count)


