def text_match_two_three(text: str) -> bool:
  if 'a' in text and text.count('b') in [2,3]:
    return True
  else:
    return False