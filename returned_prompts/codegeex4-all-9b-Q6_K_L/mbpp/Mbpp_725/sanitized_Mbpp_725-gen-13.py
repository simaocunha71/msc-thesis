def extract_quotation(s: str) -> list:
  return [i[1:-1] for i in s.split('"') if i]