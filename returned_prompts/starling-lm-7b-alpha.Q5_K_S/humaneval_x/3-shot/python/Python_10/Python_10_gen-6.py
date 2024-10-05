    if len(string) == 0:
        return ""

    def is_palindrome_suffix(s: str) -> bool:
        return s == s[::-1]

    def longest_palindrome_suffix(s: str) -> str:
        length = len(s)
        result = ""
        for i in range(length):
            if is_palindrome_suffix(s[i:]):
                result = s[i:]
        return result

    palindrome_suffix = longest_palindrome_suffix(string)
    prefix = string[:-len(palindrome_suffix)]
    return prefix + palindrome_suffix + prefix[::-1]


