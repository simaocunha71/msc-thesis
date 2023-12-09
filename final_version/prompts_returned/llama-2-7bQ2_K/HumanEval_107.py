
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    even_odd = (1,)
    s = ""
    for i in range(n):
        if ispalin(i*1):
            even_odd[0] += 1
            s += str(i*1) + " "
        elif ispalin(str(i)):
            even_odd[1] += 1
            s += str(str(i)) + " "
    even_odd = tuple(even_odd)
    return even_odd

n = 60
print("The even and odd palindromes numbers within range (1, ", n, ") are", end="\n")
for i in even_odd(n):
    print(*i, end="\t")
