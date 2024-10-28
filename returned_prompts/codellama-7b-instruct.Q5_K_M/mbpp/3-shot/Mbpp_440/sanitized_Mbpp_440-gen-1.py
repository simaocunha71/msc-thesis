def find_adverb_position(sentence):
  for i, word in enumerate(sentence.split()):
    if word.endswith('ly'):
      return (i, len(word)-2, word)
  return (None, None, None)