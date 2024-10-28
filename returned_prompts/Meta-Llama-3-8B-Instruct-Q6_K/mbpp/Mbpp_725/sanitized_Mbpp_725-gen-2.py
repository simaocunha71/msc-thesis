def extract_quotation(s):
    return [i.strip('"') for i in s.split('"') if i.strip('"')]