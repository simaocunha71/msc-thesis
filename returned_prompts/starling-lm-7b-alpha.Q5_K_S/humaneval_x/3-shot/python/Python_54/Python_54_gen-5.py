    if len(s0) != len(s1):
        return False

    # count each character in the first string
    char_counts = {}
    for c in s0:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    # check each character in the second string
    for c in s1:
        if c not in char_counts or char_counts[c] == 0:
            return False
        else:
            char_counts[c] -= 1

    return True


