def largest_subset(lst):
    if len(lst) == 1:
        return 1
    if len(lst) == 2:
        return 1 if lst[0] % lst[1] == 0 or lst[1] % lst[0] == 0 else 0

    max_size = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % lst[j] == 0 or lst[j] % lst[i] == 0:
                subset = [lst[i], lst[j]]
                size = 1
                for k in range(len(lst)):
                    if k not in (i, j) and lst[i] % lst[k] == 0 or lst[k] % lst[i] == 0:
                        subset.append(lst[k])
                        size += 1
                max_size = max(max_size, size)

    return max_size