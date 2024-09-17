def extract_quotation(s: str):
  return [i for i in s.split('"') if i != '']