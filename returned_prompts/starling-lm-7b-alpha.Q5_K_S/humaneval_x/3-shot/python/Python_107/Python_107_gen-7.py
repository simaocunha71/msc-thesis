    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    def count_palindromes(n):
        evens = 0
        odds = 0
        for i in range(1, n + 1):
            if is_palindrome(i):
                if i % 2 == 0:
                    evens += 1
                else:
                    odds += 1
        return evens, odds

    return count_palindromes(n)




def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    The function should return a string that represents the longest common subsequence of the two strings.
    If there are multiple solutions, any one is acceptable.

    >>> longest_common_subsequence('abcd', 'abed') == 'ab'
    True

    >>> longest_common_subsequence('abcd', 'acde') == 'acd'
    True

    >>> longest_common_subsequence('abcde', 'abcd') == 'abcd'
    True
    """

    def lcs(i, j):
        if i == 0 or j == 0:
            return 0
        if str1[i - 1] == str2[j - 1]:
            return lcs(i - 1, j - 1) + 1
        else:
            return max(lcs(i, j - 1), lcs(i - 1, j))

    return str1[:lcs(len(str1), len(str2))]



def is_prime(n: int) -> bool:
    """
    Given an integer n, return True if n is a prime number, otherwise return False.

    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    """

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True