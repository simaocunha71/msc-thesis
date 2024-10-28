
def find_adverb_position(sentence: str):
    adverbs = ["quickly", "clearly", "gently", "slowly"]
    for i, word in enumerate(sentence.split()):
        if word in adverbs:
            return i, word
    return None, None


