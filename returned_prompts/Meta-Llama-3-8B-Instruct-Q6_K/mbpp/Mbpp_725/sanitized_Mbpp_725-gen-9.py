def extract_quotation(s):
    return [s[s.find('"')+1:s.rfind('"')].replace(" ", "") for s in s.split('"') if s != '']