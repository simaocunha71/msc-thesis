def even_position(lst: list) -> bool:
    return all(i % 2 == 0 for i in lst[::2])