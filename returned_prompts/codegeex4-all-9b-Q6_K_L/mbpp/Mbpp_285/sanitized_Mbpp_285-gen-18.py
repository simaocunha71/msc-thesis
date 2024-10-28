def text_match_two_three(s: str) -> bool:
  return bool(re.match(r'ab{2,3}', s))