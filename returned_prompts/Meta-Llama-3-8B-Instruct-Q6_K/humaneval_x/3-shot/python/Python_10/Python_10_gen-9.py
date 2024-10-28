    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def make_palindrome(s: str) -> str:
        if is_palindrome(s):
            return s

        for i in range(len(s)):
            postfix = s[i:]
            if is_palindrome(postfix):
                return s + s[:i][::-1]

        return s + s[::-1]  # if no palindrome postfix found, return original string with reverse prefix


