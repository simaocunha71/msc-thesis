
def find_max(words):
    words.sort()  # sort the list in lexicographical order
    max_unique = 0
    max_word = ''
    for word in words:
        unique = len(set(word))  # count unique characters in a word
        if unique > max_unique:
            max_unique = unique
            max_word = word
    return max_word

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))

# output:
# string
# enam
# aaaaaaa

This solution works by iterating over the list of words, and for each word, it computes the set of unique characters in the word (which removes duplicates). It then compares the length of this set to the current maximum unique character count. If the word has more unique characters, it updates the maximum unique count and the corresponding word. It finally returns the word with the maximum unique character count. If there are multiple words with the same maximum unique character count, it returns the one that comes first in lexicographical order.
<jupyter_output>
<empty_output>
<jupyter_text>
5. Write a function that takes a number and returns a list of its digits.
<jupyter_code>
