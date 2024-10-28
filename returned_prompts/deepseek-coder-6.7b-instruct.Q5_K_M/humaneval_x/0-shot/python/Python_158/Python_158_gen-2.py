
def find_max(words):
    max_unique = 0
    max_word = ''
    for word in words:
        num_unique = len(set(word))
        if num_unique > max_unique:
            max_unique = num_unique
            max_word = word
        elif num_unique == max_unique:
            max_word = min(word, max_word)
    return max_word

# Test cases
print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # "aaaaaaa"

# This solution works by iterating over each word in the input list. For each word, it creates a set of its characters to eliminate duplicates and finds the number of unique characters. If this number is greater than the current maximum unique character count, it updates the maximum count and the word with the maximum unique characters. If the number of unique characters is equal to the current maximum, it updates the word with maximum unique characters if the current word lexicographically precedes the existing word. The function finally returns the word with the maximum number of unique characters.
<jupyter_output>
string
enam
aaaaaaa
<jupyter_text>
Question 5
<jupyter_code>
