def extract_quotation(s: str) -> list:
    return [x.strip() for x in s.split('"') if x.strip() != '']

