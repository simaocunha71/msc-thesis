def cummulative_sum(tuples: list) -> int:
    total = 0
    for tup in tuples:
        total += sum(tup)
    return total

