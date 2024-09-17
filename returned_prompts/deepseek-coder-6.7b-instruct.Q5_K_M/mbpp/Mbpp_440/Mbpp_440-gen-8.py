
import re
def find_adverb_position(sentence):
    adverbs = re.finditer(r'\b(always|often|usually|often|easily|simply|quickly|today|just|here|now|well|sure|actually)\b', sentence)
    for adverb in adverbs:
        return (adverb.start(),adverb.end(),adverb.group())


