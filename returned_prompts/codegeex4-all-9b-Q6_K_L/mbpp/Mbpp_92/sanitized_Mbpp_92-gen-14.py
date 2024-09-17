def is_undulating(n: int) -> bool:
    num_str = str(n)
    if len(num_str) < 3:
        return False
    pattern = num_str[0] + num_str[1]
    for i in range(2, len(num_str), 2):
        if num_str[i] != pattern[0] or num_str[i+1] != pattern[1]:
            return False
    return True