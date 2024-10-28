
def find_max(words):
    max_unique_chars = 0
    max_word = ''
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars:
            max_word = min(word, max_word)
    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # "aaaaaaa"

# In the function find_max, we iterate over the list of words. For each word, we calculate the number of unique characters in it by converting the word to a set (which removes duplicates) and then get the length of the set. If the number of unique characters of the current word is greater than the current maximum, we update the maximum and the corresponding word. If the number of unique characters is equal to the current maximum, we compare the words and keep the lexicographically smallest one. At the end, we return the word with the maximum number of unique characters.
<jupyter_output>
string
enam
aaaaaaa
<jupyter_text>
Problem 3:
<jupyter_code>
