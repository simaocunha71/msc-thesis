def pack_consecutive_duplicates(lst):
    result = []
    i = 0
    while i < len(lst):
        count = 1
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            i += 1
            count += 1
        result.append(lst[i] * [lst[i]] for _ in range(count))
        i += 1
    return [item for sublist in result for item in sublist]  # flatten the list of lists