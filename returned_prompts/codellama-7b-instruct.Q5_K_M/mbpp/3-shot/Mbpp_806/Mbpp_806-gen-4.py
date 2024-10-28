
def max_run_uppercase(s: str) -> int:
    longest = 0
    current = 0
    for c in s:
        if c.isupper():
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return longest


