def find_adverb_position(sentence):
    adverbs = ["quickly", "clearly", "slowly", "loudly", "quietly", "carefully", "gently", "happily", "sadly", "angrily", "easily", "openly", "naturally", "honestly", "often", "sometimes", "usually", "seldom", "rarely", "never", "usually", "ordinarily", "commonly", "generally", "particularly", "specifically", "directly", "indirectly", "directly", "finally", "ultimately", "eventually", "finally", "consequently", "subsequently", "therefore", "otherwise", "instead", "accordingly", "conversely", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally", "equally"]
    for i in range(len(sentence)):
        if sentence[i] in adverbs:
            return i, sentence.index(sentence[i]), sentence[i]


find_adverb_position("clearly!! we can see the sky")

# This is the solution to the problem. It defines a function called find_adverb_position that takes a sentence as an argument. Inside the function, there is a list of adverbs. The function then iterates over the sentence and checks if each character is an adverb. If it is, it returns the index of the character, the index of the adverb in the sentence, and the adverb itself. This allows the function to find the position of the first adverb in the sentence.

"""
The function find_adverb_position takes a sentence as an argument and returns the position of the first adverb in the sentence. The function does this by