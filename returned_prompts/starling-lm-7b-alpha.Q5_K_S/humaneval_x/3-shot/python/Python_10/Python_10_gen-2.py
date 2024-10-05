    def longest_palindrome_postfix(s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return s[left:right + 1]

    def shortest_prefix(s: str) -> str:
        return s[:len(s) - len(longest_palindrome_postfix(s))]

    prefix = shortest_prefix(string)
    if prefix == '':
        return string + string[::-1]
    else:
        return string + string[:len(prefix)][::-1]


