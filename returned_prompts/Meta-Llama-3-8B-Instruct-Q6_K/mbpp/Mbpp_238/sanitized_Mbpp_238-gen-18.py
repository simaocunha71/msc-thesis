def number_of_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substrings.add(s[i: j+1])
    return len(substrings)