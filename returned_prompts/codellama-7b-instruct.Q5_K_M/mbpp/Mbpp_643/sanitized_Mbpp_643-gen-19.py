def text_match_wordz_middle(text: str) -> bool:
  if "z" in text and text.startswith("z") and text.endswith("z"):
    return True
  else:
    return False