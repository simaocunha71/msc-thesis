def text_match_two_three(text: str) -> bool:
  if 'a' in text and 'b' in text:
    if 'b' in text[text.index('a')+1:text.index('a')+3]:
      return True
    else:
      return False
  else:
    return False