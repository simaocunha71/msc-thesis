import re
def find_adverb_position(sentence):
  adverb = re.findall(r'\b\w+\b', sentence)
  for i, word in enumerate(adverb):
    if word.endswith('ly'):
      return i, len(word), word
  return None

