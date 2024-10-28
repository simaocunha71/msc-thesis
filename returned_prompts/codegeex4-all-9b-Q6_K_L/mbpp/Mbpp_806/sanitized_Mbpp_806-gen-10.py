def max_run_uppercase(s: str) -> int:
    if not s:
        return 0
    max_count = 0
    current_count = 0
    for char in s:
        if char.isupper():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count