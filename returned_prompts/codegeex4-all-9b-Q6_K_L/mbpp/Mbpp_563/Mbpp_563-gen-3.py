def extract_values(s: str) -> list:
  return [x.strip('"') for x in s.split(',')]


