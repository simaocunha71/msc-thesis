    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def longest_palindrome_suffix(s: str) -> str:
        for i in range(len(s), -1, -1):
            if is_palindrome(s[i:]):
                return s[:i]

    prefix = longest_palindrome_suffix(string)
    return prefix + prefix[::-1] if prefix else string + string[::-1]  # for empty string


