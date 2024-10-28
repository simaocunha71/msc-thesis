def find_adverb_position(sentence):
  words = sentence.split()
  for i, word in enumerate(words):
    if word.endswith('ly'):
      return (i, len(word)-2, word)
  return (None, None, None)