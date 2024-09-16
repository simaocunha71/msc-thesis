def extract_quotation(string):
    return [part[1:-1] for part in string.split('"') if part]
