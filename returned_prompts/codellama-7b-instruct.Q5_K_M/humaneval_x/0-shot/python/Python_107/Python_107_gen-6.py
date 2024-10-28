
    def even_odd_palindrome(n):
        """
        :type n: int
        :rtype: Tuple[int, int]
        """
        count_even = 0
        count_odd = 0
        for i in range(1, n+1):
            if is_palindrome(i) and is_even(i):
                count_even += 1
            elif is_palindrome(i) and is_odd(i):
                count_odd += 1
        return (count_even, count_odd)

    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return n % 2 == 1