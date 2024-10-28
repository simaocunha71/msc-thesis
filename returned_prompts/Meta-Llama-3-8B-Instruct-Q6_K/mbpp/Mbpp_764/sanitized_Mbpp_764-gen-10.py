def number_ctr(s: str) -> int:
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count