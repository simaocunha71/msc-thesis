def remove_length(str: str,k: int) -> str:
  new_str = ''
  for word in str.split():
    if len(word) != k:
      new_str += word + ' '
  return new_str.strip()