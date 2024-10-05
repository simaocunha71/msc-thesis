    def expand_around_center(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    start = 0
    for i in range(len(s)):
        palindrome = expand_around_center(s, i, i)
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            start = i

       