import re
def find_adverb_position(sentence):
  pattern = r'\b(adverb)\b'
  match = re.search(pattern, sentence, re.IGNORECASE)
  if match:
    return match.start(), match.end(), match.group()
  else:
    return None