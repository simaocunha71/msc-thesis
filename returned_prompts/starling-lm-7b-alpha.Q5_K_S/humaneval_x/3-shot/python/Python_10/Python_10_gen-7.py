    def longest_palindromic_substring(s: str) -> str:
        if len(s) == 0:
            return ''

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1

        while not is_palindrome(start, end):
            start -= 1
            end += 1

        return s[start:end + 1]

    suffix = longest_palindromic_substring(string)
    prefix = string[:len(string) - len(suffix)]

    return prefix + suffix + prefix[::-1]


