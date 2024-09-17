
def text_match_wordz_middle(text: str) -> bool:
  return text.count('z') == text.count('z', 1, -1)


