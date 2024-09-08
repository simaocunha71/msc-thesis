def capital_words_spaces(s: str):
    return ' '.join(s.split())

print(capital_words_spaces("Python"))
print(capital_words_spaces("ThisIsASentence"))
print(capital_words_spaces("ThisIsNotASentence"))
print(capital_words_spaces("THISISNOTASENTENCE"))

# Output:
# Python
# This Is A Sentence
# This Is Not A Sentence
# THIS IS NOT AS ENTENCE


"""
