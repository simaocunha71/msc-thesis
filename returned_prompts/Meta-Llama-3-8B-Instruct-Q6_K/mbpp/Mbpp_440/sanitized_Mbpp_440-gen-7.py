import re
def find_adverb_position(sentence):
  adverbs = ['quickly', 'loudly', 'brightly', 'clearly', 'gently', 'wisely']
  for adverb in adverbs:
    match = re.search(r'\b' + re.escape(adverb) + r'\b', sentence)
    if match:
      return (match.start(), match.end(), adverb)
  return None