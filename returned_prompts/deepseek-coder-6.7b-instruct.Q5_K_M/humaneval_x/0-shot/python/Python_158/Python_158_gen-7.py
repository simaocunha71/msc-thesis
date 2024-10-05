
def find_max(words):
    max_unique = 0
    max_word = ''
    for word in words:
        num_unique = len(set(word))
        if num_unique > max_unique:
            max_unique = num_unique
            max_word = word
        elif num_unique == max_unique:
            if word < max_word:
                max_word = word
    return max_word

print(find_max(["name", "of", "string"]))  # == "string"
print(find_max(["name", "enam", "game"]))  # == "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"]))  # == "aaaaaaa"

# In this solution, we iterate through each word in the list. For each word, we create a set of unique characters (by converting the word to a set), and find out how many unique characters it has. If this number is greater than the current maximum number of unique characters we have found, we update the maximum number of unique characters and the word that corresponds to it. If the number of unique characters is equal to the current maximum, we check if the current word comes before the word that we have found so far in lexicographical order. If it does, we update the word that we have found. Finally, we return the word that we have found with the maximum number of unique characters.
<jupyter_output>
string
enam
aaaaaaa
<jupyter_text>
Problem 6:
<jupyter_code>
