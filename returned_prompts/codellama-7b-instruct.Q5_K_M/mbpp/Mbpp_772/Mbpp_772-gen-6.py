
def remove_length(my_str: str, k: int) -> str:
  return ' '.join([word for word in my_str.split() if len(word) != k])


