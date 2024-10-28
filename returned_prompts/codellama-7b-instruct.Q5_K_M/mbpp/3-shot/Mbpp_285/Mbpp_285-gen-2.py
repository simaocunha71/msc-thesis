
def text_match_two_three(text: str) -> bool:
  if text.count('a') > 0:
    if text.count('b') == 2 or text.count('b') == 3:
      return True
  return False


