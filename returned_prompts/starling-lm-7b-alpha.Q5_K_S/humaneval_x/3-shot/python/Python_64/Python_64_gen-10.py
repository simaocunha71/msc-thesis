    vowel_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, 'y': True}
    count = 0
    for c in s:
        if vowel_map.get(c, False):
            count += 1
    return count


