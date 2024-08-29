def extract_quotation(s):
    return [i for i in s.split() if i.startswith('"')]