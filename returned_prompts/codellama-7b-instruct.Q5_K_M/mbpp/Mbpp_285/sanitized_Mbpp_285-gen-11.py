def text_match_two_three(text):
  if 'a' in text:
    if text.count('b') in range(2,4):
      return True
    else:
      return False
  else:
    return False