def replace_specialchar(str: str) -> str:
  return str.replace(' ', ':').replace(',', ':').replace('.', ':').strip(':')