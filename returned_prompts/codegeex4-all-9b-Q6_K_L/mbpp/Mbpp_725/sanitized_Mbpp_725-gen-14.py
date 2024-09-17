def extract_quotation(s: str):
    return [i.strip() for i in s.split('"') if i]