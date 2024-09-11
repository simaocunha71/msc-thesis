def text_match_three(text: str) -> bool:
  return text[0] == 'a' and len(text) > 1 and text[1:4] == 'bb' and text[4:] == ''