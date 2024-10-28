    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def count_palindrome(num, is_even):
        count = 0
        for i in range(1, num + 1):
            if is_palindrome(i) and (is_even and i % 2 == 0 or not is_even and i % 2 != 0):
                count += 1
        return count

    return count_palindrome(n, True), count_palindrome(n, False)


