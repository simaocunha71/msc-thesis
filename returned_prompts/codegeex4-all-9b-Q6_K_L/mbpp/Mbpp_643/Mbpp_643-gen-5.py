def text_match_wordz_middle(text: str) -> bool:
  text = text.strip()
  if text[0] == 'z' or text[-1] == 'z':
    return False
  if 'z' in text[1:-1]:
    return True
  return False

