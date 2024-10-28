def find_adverb_position(sentence):
  for word in sentence.split():
    if word.endswith('ly'):
      return sentence.index(word), sentence.index(word) + len(word), word
  return None

