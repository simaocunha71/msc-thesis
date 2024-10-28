def remove_uppercase(s: str) -> str:
  return ''.join([i for i in s if not i.isupper()])