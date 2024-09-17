def text_match_wordz_middle(text: str) -> bool:
  if len(text) <= 2:
    return False
  return 'z' in text[1:-1]