def first_repeated_char(s: str):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

print(first_repeated_char("abcabc"))  # "a"

# Solution 2: Using list as a stack
