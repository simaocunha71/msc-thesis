def text_match_two_three(text: str) -> bool:
  if 'a' in text and ('b' in text and len(text.split('b')) == 2 or len(text.split('b')) == 3):
    return True
  return False