import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(ly|quickly|loudly|happily|slowly|quietly|silently|swiftly|carefully|loudly|strongly|weirdly|gently|rapidly|instantly|exactly|completely|partially|somewhat|entirely|almost|not|never|always|ever|often|usually|sometimes|rarely|seldom|hardly|scarcely|barely|just|merely|simply|only|justly|fairly|roughly|approximately|exactly|precisely|approximately|roughly|notably|obviously|clearly|immediately|directly|indirectly|literally|figuratively|essentially|basically|generally|specifically|essentially|basically|generally|specifically)\b', sentence)
    if adverbs:
        return (0, sentence.index(adverbs[0]), adverbs[0])
    else:
        return None