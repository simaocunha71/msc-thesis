    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def count_palindromes(num):
        return sum(is_palindrome(i) for i in range(1, num + 1))

    total_palindromes = count_palindromes(n)
    even_palindromes = total_palindromes // 2
    odd_palindromes = total_palindromes // 2 + total_palindromes % 2

    return even_palindromes, odd_palindromes


