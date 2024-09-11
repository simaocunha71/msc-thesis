def longest_substring(s):
    seen = set()
    max_len = 0
    start = 0

    for i, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        seen[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len


"""