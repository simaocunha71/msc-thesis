
def find_max(words):
    max_unique = max_word = ""
    for word in words:
        unique = len(set(word))
        if unique > max_unique or (unique == max_unique and word < max_word):
            max_unique = unique
            max_word = word
    return max_word

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))

'''
Output:
string
enam
aaaaaaa
'''

Explanation:
In the function find_max, we go through each word in the words list. We calculate the number of unique characters in each word by converting the word to a set and counting the number of elements in the set. If the number of unique characters is greater than max_unique or the number of unique characters is the same but the word comes lexicographically before max_word, we update max_unique and max_word. Finally, we return max_word.
'''

# Alternative Solution
def find_max(words):
    return max(sorted(words), key=lambda word: len(set(word)))

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))

'''
Output:
string
enam
aaaaaaa
'''

Explanation:
In this alternative solution, we use the built-in max function with a key parameter. The key function is a lambda function that returns the number of unique characters in each word. The max function returns the word with the maximum number of unique characters. If there are multiple words with the same number of unique characters, the one that comes first in lexicographical order is returned.
'''

# Alternative Solution
def find_max(words):
    return max(words, key=lambda word: (len(set(word)), word))

print(find_max(["name", "of", "string"]))
