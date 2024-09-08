def longest_common_prefix(strings):
    if not strings:
        return ""

    shortest = min(strings, key=len)

    for i, char in enumerate(shortest):
        for other in strings:
            if other[i] != char:
                return shortest[:i]

    return shortest

print