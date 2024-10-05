    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    def count_palindromes(x, is_even):
        count = 0
        for i in range(1, x + 1):
            if is_palindrome(i) and (is_even and i % 2 == 0 or not is_even and i % 2 == 1):
                count += 1
        return count

    return count_palindromes(n, False), count_palindromes(n, True)


