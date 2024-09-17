def count_reverse_pairs(words: list) -> int:
    count = 0
    for word in words:
        if word[::-1] in words:
            count += 1
    return count