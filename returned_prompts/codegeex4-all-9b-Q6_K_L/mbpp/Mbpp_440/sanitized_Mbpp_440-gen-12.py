import re
def find_adverb_position(sentence: str) -> tuple:
  adverb = re.findall(r'\w+ly', sentence)
  if adverb:
    position = sentence.index(adverb[0])
    return (position, position + len(adverb[0]), adverb[0])
  else:
    return None