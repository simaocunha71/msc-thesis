def is_samepatterns(patterns: list, strs: list) -> bool:
    for i in range(len(patterns)):
        if not patterns[i] == strs[i]:
            return False
    return True