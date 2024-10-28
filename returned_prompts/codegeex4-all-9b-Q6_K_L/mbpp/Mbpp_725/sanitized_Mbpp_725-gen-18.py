def extract_quotation(text: str) -> list:
  return text.split('"')[1::2]