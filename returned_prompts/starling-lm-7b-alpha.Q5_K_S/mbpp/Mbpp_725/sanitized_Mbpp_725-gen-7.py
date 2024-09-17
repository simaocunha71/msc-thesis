def extract_quotation(s):
    quotes = []
    while True:
        i = s.find('"')
        if i == -1:
            break
        j = s.find('"', i + 1)
        if j == -1:
            break
        quotes.append(s[i + 1: j])
        s = s[:i] + s[j:]
    return quotes