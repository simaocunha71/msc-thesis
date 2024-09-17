def extract_quotation(s: str) -> list:
  return [i.strip() for i in s.split('"') if i.strip()]