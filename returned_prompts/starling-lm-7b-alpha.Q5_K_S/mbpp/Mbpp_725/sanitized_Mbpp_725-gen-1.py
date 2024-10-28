def extract_quotation(s):
    l = []
    while True:
        if s.find('"') == 0:
            break
        i = s.find('"')
        j = s.find('"', i + 1)
        l.append(s[i + 1 : j])
        s = s[j:]
    return l