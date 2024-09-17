def text_match_two_three(text: str) -> bool:
  match = re.search(r'a(b{2,3})', text)
  return bool(match)