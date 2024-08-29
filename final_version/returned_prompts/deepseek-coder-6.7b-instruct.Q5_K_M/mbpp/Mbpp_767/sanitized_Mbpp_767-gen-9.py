def get_pairs_count(lst, sum):
    map = {}
    twice_count = 0
    for el in lst:
        if el in map:
            map[el] += 1
        else:
            map[el] = 1
    for el in lst:
        twice_count += map[sum - el]
        if sum - el == el:
            twice_count -= 1
    return int(twice_count / 2)