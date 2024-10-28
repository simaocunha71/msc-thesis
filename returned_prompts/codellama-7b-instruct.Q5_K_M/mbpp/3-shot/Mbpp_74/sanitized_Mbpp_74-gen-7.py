def is_samepatterns(my_list: list, patterns: list) -> bool:
    if len(my_list) != len(patterns):
        return False
    for i in range(len(my_list)):
        if my_list[i] != patterns[i % len(patterns)]:
            return False
    return True