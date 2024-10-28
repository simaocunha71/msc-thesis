
def find_adverb_position(sentence):
  adverbs = ["quickly", "clearly", "rapidly", "easily", "slowly"]
  for i in range(len(sentence)):
    if sentence[i].lower() in adverbs:
      return i, sentence[i], sentence
  return None, None, None


