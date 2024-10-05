    def longest_palindromic_substring(s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        max_length = 1
        start = 0
        for i in range(len(s)):
            # odd length palindrome
            l, h = i, i
            while l >= 0 and h < len(s) and s[l] == s[h]:
                if h - l + 1 > max_length:
                    start = l
                    max_length = h - l + 1
                l -= 1
                h += 1

            # even length palindrome
            l, h = i, i + 1
            while l >= 0 and h < len(s) and s[l] == s[h]:
                if h - l + 1 > max_length:
                    start = l
                    max_length = h - l + 1
                l -= 1
                h += 1
        return s[start:start + max_length]

    palindromic_suffix = longest_palindromic_substring(string)
    prefix = string[:-len(palindromic_suffix)]
    return prefix + palindromic_suffix + prefix[::-1]


def make_palindrome_v2(string: str) -> str:
    def find_longest_palindrome(s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        max_length = 0
        longest_palindrome = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd_length_palindrome = find_longest_palindrome_helper(s, i, i)
            if len(odd_length_palindrome) > max_length:
                max_length = len(odd_length_palindrome)
                longest_palindrome = odd_length_palind