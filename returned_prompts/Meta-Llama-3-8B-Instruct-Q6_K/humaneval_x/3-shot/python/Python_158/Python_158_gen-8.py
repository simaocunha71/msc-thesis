    def find_max(words):
        max_word = max(words, key=lambda x: (len(set(x)), x))
        return max_word
    # test cases
    print(find_max(["name", "of", "string"])) # "string"
    print(find_max(["name", "enam", "game"])) # "enam"
    print(find_max(["aaaaaaa", "bb" ,"cc"])) # "aaaaaaa"


