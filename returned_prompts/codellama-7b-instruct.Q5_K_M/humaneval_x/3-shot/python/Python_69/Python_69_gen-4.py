    max_count = -1
    max_value = -1
    for i in range(1, len(lst) + 1):
        count = 0
        for j in range(len(lst)):
            if lst[j] == i:
                count += 1
                if count >= i and count > max_count:
                    max_count = count
                    max_value = i
    if max_value == -1:
        return max_value
    else:
        return max_value


