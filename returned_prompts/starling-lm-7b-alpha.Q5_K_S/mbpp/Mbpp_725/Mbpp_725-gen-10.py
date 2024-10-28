
def extract_quotation(s):
    quotes = []
    i = 0
    while i < len(s):
        if s[i] == '"':
            quotes.append(s[i+1:s.index('"',i+1)])
            i = s.index('"',i+1)
        i += 1
    return quotes


