def extract_quotation(s: str) -> list:
  return [i for i in s.split('"')[1::2]]