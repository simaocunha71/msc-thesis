def find_max(words):
    max_len = 0
    max_word = ""

    for word in words:
        char_set = set(word)
        if len(char_set) > max_len:
            max_len = len(char_set)
            max_word = word
        elif len(char_set) == max_len:
            if word < max_word:
                max_word = word

    return max_word
# test cases
print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # "aaaaaaa"




# Explanation:
# This function iterates over the list of words. For each word, it calculates the set of unique characters (char_set).
# If the length of char_set is greater than the current maximum length (max_len), it updates max_len and max_word.
# If the length of char_set is equal to max_len, it checks if the current word is lexicographically less than the current max_word, and if so, updates max_word.
# Finally, it returns the word with the maximum number of unique characters.
# The time complexity is O(NM), where N is the number of words and M is the maximum length of a word, because we're iterating over the words and for each word, we're calculating the set of unique characters.
# The space complexity is O(M), because we're storing the set of unique characters for each word, and the maximum size of this set is equal to the maximum length of a word.