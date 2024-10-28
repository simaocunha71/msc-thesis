
def find_adverb_position(sentence: str) -> tuple:
  for i in range(len(sentence)):
    if sentence[i] in ".,!?":
      yield i, sentence[i]
    if sentence[i] in "w,h,a,y,o":
      yield i+1, sentence[i+1]


