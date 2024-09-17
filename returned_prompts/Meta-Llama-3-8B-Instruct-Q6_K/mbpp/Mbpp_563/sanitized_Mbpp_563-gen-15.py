def extract_values(s):
    result = []
    start = end = 0
    while True:
        start = s.find('"', start)
        if start == -1:
            break
        end = s.find('"', start + 1)
        result.append(s[start + 1:end])
        start = end + 1
    return result