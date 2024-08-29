
def anagrams(word, words):
    sorted_word = sorted(word)
    anagrams = [w for w in words if sorted(w) == sorted_word]
    return anagrams

print(anagrams('listen', ['enlist', 'google', 'inlets', 'silent']))
assert anagrams('listen', ['enlist', 'google', 'inlets', 'silent'])==['