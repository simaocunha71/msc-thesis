
def find_adverb_position(sentence:str):
  adverbs = ["quickly", "clearly", "slowly", "beautifully"]
  for i in range(len(sentence)):
    if sentence[i] in adverbs:
      return i, sentence[i], sentence
  return None


