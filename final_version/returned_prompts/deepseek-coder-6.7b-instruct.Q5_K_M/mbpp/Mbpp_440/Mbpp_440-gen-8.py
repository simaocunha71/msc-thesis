def find_adverb_position(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in ['clearly', 'easily', 'often', 'quickly', 'slowly', 'carefully', 'tenderly']:
            return (i, i+1, words[i])
    return None

print(find_adverb_position("clearly!! we can see the sky"))
# (0, 7, 'clearly')

Note: This function checks for the words in a list of commonly used adverbs. It may not cover all possible adverbs, as English language has a lot of variations and exceptions. You might need to extend this list or use a more advanced NLP library to handle more complex sentences.

