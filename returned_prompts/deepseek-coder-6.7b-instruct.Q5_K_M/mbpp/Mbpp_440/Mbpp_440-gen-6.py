
import re
def find_adverb_position(sentence: str) -> tuple:
  adverbs = re.findall(r'\b(always|usually|often|oftenly|simply|simplyly|just|justly|kindly|kindlyly|never|rarely|seldom|seldomly|now|then|thereupon|thereafter|thereof|thereon|thereby)\b', sentence)
  if adverbs:
    adverb = adverbs[0]
    position = sentence.index(adverb)
    return position, position+len(adverb), adverb
  else:
    return 'No adverb found'


