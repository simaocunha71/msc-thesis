    def longest_palindromic_substring(s: str) -> str:
        result = ''
        for idx in range(len(s)):
            left = s[idx:idx+1:]
            right = s[::-1][:len(left):]
            if left == right and len(left) > len(result):
                result = left

        return result

    prefix = string[:len(string) // 2]
    suffix = longest_palindromic_substring(string[::-1][len(string) // 2:])
    return prefix + suffix + prefix[::-1]


