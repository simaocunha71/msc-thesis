
def find_adverb_position(sentence):
  adverb_positions = []
  adverbs = ["well", "quickly", "clearly", "quickly", "easily", "slowly"]
  for word in sentence.split():
    if word in adverbs:
      adverb_positions.append((adverbs.index(word), len(adverb_positions), word))
  return adverb_positions[0] if adverb_positions else (-1, -1, '')


