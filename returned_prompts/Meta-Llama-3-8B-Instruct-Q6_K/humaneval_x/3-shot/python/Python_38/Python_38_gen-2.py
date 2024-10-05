    result = []
    for group in [s[i:i+3] for i in range(0, len(s), 3)]:
        if len(group) == 3:
            result.append(group[2] + group[0] + group[1])
        else:
            result.append(group)
    return ''.join(result)  # join all groups into a single string
    # return ''.join(result).replace(' ', '')  # remove any remaining spaces
    # return result  # return list of groups if you want
    # return ' '.join(result)  # join all groups into a single string with spaces in between


