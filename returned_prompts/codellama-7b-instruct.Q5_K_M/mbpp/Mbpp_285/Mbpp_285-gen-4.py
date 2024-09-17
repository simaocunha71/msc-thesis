
def text_match_two_three(text: str) -> bool:
  if 'a' in text:
    if text.count('b') == 2 or text.count('b') == 3:
      return True
  return False


