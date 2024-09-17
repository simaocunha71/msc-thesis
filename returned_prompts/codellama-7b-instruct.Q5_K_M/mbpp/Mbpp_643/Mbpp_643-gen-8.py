
def text_match_wordz_middle(text: str) -> bool:
  if text.startswith('z'):
    text = text[1:]
  if text.endswith('z'):
    text = text[:-1]
  return 'z' in text


