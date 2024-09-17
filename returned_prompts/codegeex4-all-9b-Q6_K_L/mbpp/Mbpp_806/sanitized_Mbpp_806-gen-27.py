def max_run_uppercase(s: str) -> int:
    count = 0
    max_count = 0
    for char in s:
        if char.isupper():
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)