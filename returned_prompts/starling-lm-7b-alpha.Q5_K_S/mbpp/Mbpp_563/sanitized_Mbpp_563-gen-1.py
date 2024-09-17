def extract_values(s):
    index = 0
    values = []
    while index < len(s):
        start = index
        index = s.find('"', start) + 1
        end = s.find('"', index)
        values.append(s[index:end])
    return values