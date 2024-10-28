def odd_position(lst: list) -> bool:
    return all(lst[i] % 2 == 1 for i in range(1, len(lst), 2))