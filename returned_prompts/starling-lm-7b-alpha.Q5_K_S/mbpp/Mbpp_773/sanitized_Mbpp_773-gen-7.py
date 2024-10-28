def occurance_substring(s, w):
    # Your code here
    index = []
    for i in range(len(s)):
        if s[i:i+len(w)] == w:
            index.append((w, i, i+len(w)-1))
    if not index:
        return None
    else:
        return index