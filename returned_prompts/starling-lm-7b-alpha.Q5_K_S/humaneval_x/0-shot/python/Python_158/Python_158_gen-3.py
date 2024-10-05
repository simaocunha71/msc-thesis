
def find_max(words):
    def count_unique(word):
        word = set(word)
        return len(word)

    max_count = 0
    max_word = ""
    for w in words:
        if count_unique(w) > max_count:
            max_count = count_unique(w)
            max_word = w
        elif count_unique(w) == max_count:
            if w < max_word:
                max_word = w
    return max_word

print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"])) # "aaaaaaa"





def find_max(words):
    def count_unique(word):
        word = set(word)
        return len(word)

    max_count = 0
    max_word = ""
    for w in words:
        if count_unique(w) > max_count:
            max_count = count_unique(w)
            max_word = w
        elif count_unique(w) == max_count:
            if w < max_word:
                max_word = w
    return max_word

print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"])) # "aaaaaaa"


















































































































