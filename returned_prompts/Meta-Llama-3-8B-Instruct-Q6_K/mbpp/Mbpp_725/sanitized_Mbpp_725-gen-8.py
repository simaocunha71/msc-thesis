def extract_quotation(s):
    return [i[1:-1] for i in s.split('"') if len(i)>1 and i[0] == '"']