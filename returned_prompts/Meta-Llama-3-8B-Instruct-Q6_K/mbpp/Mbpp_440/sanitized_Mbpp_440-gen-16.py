def find_adverb_position(sentence):
    adverbs = ["quickly", "slowly", "loudly", "softly", "clearly", "silently", "quietly", "wisely", "foolishly", "honestly"]
    words = sentence.split()
    for i, word in enumerate(words):
        if word.lower() in adverbs:
            return i, len(" ".join(words[:i])), word
    return None