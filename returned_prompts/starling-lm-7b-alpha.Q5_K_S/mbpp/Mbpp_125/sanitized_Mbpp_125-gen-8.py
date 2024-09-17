def find_length(s):
    max_length = 0
    for i in range(len(s)):
        max_length = max(max_length, i + 1 - s.find('1', 0, i + 1), i + 1 - s.find('0', 0, i + 1))
    return max_length