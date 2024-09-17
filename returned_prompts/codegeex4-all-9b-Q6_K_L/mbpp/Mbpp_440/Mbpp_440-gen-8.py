import re
def find_adverb_position(sentence: str) -> tuple:
  pattern = re.compile(r'\b(adverb)\b')
  matches = pattern.finditer(sentence)
  positions = []
  for match in matches:
    positions.append((match.start(), match.end(), match.group()))
  if positions:
    return positions[0]

