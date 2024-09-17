def text_match_wordz_middle(text: str) -> bool:
  if text.startswith("z") and text.endswith("z") and text[1:-1].find("z") != -1:
    return True
  return False