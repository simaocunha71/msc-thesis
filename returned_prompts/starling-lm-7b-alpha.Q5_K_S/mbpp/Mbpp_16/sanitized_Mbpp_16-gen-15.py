def text_lowercase_underscore(str:str) -> bool:
  if str.isalpha() and '_' in str:
    return True
  return False