
def find_max(words):
    max_unique = 0
    max_word = ""

    for word in words:
        num_unique = len(set(word))
        if num_unique > max_unique:
            max_unique = num_unique
            max_word = word
        elif num_unique == max_unique:
            max_word = min(word, max_word)

    return max_word

print(find_max(["name", "of", "string"]))  # "string"
print(find_max(["name", "enam", "game"]))  # "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # "aaaaaaa"

# The function works by iterating over each word in the list of words. For each word, it creates a set of unique characters, which will remove any duplicate letters. It then checks if the number of unique characters is greater than the current maximum unique characters count. If it is, it updates the maximum unique characters count and the word with that many unique characters. If the number of unique characters is equal to the current maximum, it checks which word comes first in lexicographical order and updates the word accordingly. Finally, it returns the word with the maximum number of unique characters.

# The function uses the set data structure to automatically remove duplicate characters from each word, which makes it efficient. It also uses the min function to determine which word comes first in lexicographical order when multiple words have the same number of unique characters.

# This function runs in O(n * m) time, where n is the number of words in the list and m is the length of the longest word. It uses O(m) space to store the sets of unique characters for each word.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 6:Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.An input string is valid if:Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.Note that an empty string is also considered valid.
<jupyter_code>