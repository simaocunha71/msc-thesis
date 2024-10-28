def text_match_wordz_middle(text: str) -> bool:
  if 'z' in text:
    if text[0] != "z" and text[-1] != "z":
      return True
  return False