def count(bools: list) -> int:
    count = 0
    for b in bools:
        if b:
            count += 1
    return count