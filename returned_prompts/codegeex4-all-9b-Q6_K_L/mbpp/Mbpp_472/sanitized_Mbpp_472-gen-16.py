def check_Consecutive(lst: list) -> bool:
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            return False
    return True