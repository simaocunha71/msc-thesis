
def find_max(words):
    max_unique_chars = 0
    max_word = ""

    for word in words:
        num_unique_chars = len(set(word))
        if num_unique_chars > max_unique_chars:
            max_unique_chars = num_unique_chars
            max_word = word
        elif num_unique_chars == max_unique_chars:
            max_word = min(max_word, word)

    return max_word

print(find_max(["name", "of", "string"]))  # == "string"
print(find_max(["name", "enam", "game"]))  # == "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # == "aaaaaaa"

In this solution, we iterate over the list of words, for each word we create a set of unique characters and find the size of that set. If this size is more than the current maximum unique characters, we update the maximum unique characters and the word with those maximum unique characters. If the size is equal to the current maximum unique characters, we update the word with lexicographically smallest order.

In the end, we return the word with the maximum number of unique characters. If there are multiple such words, we return the one that comes first in lexicographical order.

The time complexity of this solution is O(n*m), where n is the number of words and m is the average length of the words. The space complexity is O(1), because we use a constant amount of space to store the maximum unique characters and the word with those characters.
