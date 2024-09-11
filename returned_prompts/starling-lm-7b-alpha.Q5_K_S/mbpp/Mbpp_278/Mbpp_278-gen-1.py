def longest_unique_chars(s):
    d = defaultdict(int)
    for i in range(len(s)):
        if d[s[i]]:
            d.clear()
        d[s[i]] += 1
    return ''.join(s[i] for i in range(len(s)) if d[s[i]])

def longest_unique_chars(s):
    d = defaultdict(int)
    for i in range(len(s)):
        if d[s[i]]:
            d.clear()
        d[s[i]] += 1
    return ''.join(s[i] for