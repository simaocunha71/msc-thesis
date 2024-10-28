    def longest_palindromic_suffix(s: str) -> str:
        if len(s) == 0:
            return ''

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return s[left:right + 1]
            left += 1
            right -= 1

        return s

    def shortest_palindromic_prefix(s: str) -> str:
        return s[:len(s) // 2] if len(s) % 2 == 1 else s[:len(s) // 2] + s[-1]

    def make_palindromic(s: str) -> str:
        palindromic_suffix = longest_palindromic_suffix(s)
        prefix = shortest_palindromic_prefix(s)
        return s + palindromic_suffix[::-1] + prefix[::-1]

    return make_palindromic(string)


