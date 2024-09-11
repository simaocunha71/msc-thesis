def get_pairs_count(lst: list, sum_: int) -> int:
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum_:
                count += 1
    return count