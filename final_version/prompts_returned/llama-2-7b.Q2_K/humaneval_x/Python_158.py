
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def count_unique_characters(word):
        return [c for c in word if c not in setx()]


    words = sorted(list(set(words)))
    words.sort()
    max_len = 0
    max_str = ''
    for word in words:
      n_uniq_chars = count_unique_characters(word)
      if len(n_uniq_chars) > max_len:
        max_len = len(n_uniq_chars)
        max_str = word
    return max_str  # "enam"

# find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa""


words = ['enam', 'of', 'game']
print(find_max(words))
