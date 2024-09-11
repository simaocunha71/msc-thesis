def count_Pairs(lst: list, total_pairs: int) -> int:
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count
    # return sum(1 for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] != lst[j])  # alternative solution using generator expression