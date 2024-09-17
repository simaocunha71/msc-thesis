def remove_uppercase(str_in: str) -> str:
  return ''.join(filter(lambda x: x.islower(), str_in))