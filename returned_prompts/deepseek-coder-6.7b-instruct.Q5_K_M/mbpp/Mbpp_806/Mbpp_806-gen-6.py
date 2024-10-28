
def max_run_uppercase(string: str) -> int:
    current_count = 0
    max_count = 0
    for char in string:
        if char.isupper():
            current_count += 1
            max_count = max(current_count, max_count)
        else:
            current_count = 0
    return max_count


