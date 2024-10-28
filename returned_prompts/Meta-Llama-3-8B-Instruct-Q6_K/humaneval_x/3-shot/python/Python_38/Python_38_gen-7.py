    result = []
    i = 0
    while i < len(s):
        group = s[i:i+3]
        if len(group) == 3:
            result.append(group[2] + group[0] + group[1])
            i += 3
        else:
            result.append(group)
            i += 1
    return "".join(result)
    # This function works by iterating over the input string in groups of three characters.
    # If a group has three characters, it is decoded as normal (last element becomes first, first becomes second, second becomes last).
    # If a group has fewer than three characters, it is left as is.
    # The decoded groups are then joined together to form the final decoded string.