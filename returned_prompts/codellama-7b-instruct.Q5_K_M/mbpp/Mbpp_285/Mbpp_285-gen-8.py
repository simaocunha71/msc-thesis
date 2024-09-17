
def text_match_two_three(text: str) -> bool:
  if 'a' not in text:
    return False
  if text.count('b') in [2, 3]:
    return True
  return False


