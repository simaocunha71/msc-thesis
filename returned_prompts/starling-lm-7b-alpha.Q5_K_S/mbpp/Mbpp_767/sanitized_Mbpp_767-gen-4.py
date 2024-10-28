def get_pairs_count(lst, sum):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                result += 1
    return result