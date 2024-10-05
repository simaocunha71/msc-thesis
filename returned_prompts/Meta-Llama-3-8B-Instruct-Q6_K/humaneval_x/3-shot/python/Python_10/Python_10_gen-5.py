    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    for i in range(len(s), -1, -1):
        if is_palindrome(s[i:]):
            return s + s[:i][::-1]

    return s + s[::-1]  # if input is a palindrome itself
#


