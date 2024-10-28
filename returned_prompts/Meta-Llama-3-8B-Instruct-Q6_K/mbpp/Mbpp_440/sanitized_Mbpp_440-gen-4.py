import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(very|really|extremely|totally|completely|absolutely|quickly|slowly|loudly|silently|gently|roughly|smoothly|honestly|seriously|closely|farly|nearly|almost|basically|essentially|mostly|generally|usually|normally|typically|tend|prone|likely|unlikely|probably|possibly|may|might|could|would|should|can|must|shall|will|has|had|have|is|are|am|be|been|being|was|were|been|being|been|being|been|being|been|being)\b', sentence, flags=re.IGNORECASE)
    if adverbs:
        return (0, len(sentence) - len(adverbs[0]), adverbs[0])
    else:
        return None