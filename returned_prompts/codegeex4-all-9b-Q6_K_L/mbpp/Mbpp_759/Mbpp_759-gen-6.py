def is_decimal(n: str) -> bool:
  return bool(re.match(r'^\d+\.\d{2}$', n))