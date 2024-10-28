def remove_odd(s: str) -> str:
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result