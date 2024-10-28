import re
def find_adverb_position(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        if re.match(r"^(always|never|often|usually|generally|occasionally|rarely|seldom|hardly|scarcely|barely)$", word, re.IGNORECASE):
            return (i, i + len(word), word)
    return None