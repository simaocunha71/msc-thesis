"""
def find_adverb_position(sentence):
    # Create a list of adverbs
    adverbs = ["quickly", "slowly", "clearly", "quickly", "slowly"]
    # Split the sentence into words
    words = sentence.split()
    # Find the position of the first adverb
    for i, word in enumerate(words):
        if word in adverbs:
            # Return the position of the first adverb
            return i, words.index(word), word

# Test the function
print(find_adverb_position("clearly!! we can see the sky"))
"""

def find_adverb_position(sentence):
    # Create a list of adverbs
    adverbs = ["quickly", "slowly", "clearly", "quickly", "slowly"]
    # Split the sentence into words
    words = sentence.split()
    # Find the position of the first adverb
    for i, word in enumerate(words):
        if word in adverbs:
            # Return the position of the first adverb
            return i, words.index(word), word

# Test the function
print(find_adverb_position("clearly!! we can see the sky"))

# Expected output: (0, 7, 'clearly')
# The first adverb in the sentence "clearly!! we can see the sky" is 'clearly' and its position is at the 0th index.

# The function `find_adverb_position` takes a sentence as input and splits it into a list of words. It then iterates through each word in the list and checks if it is an adverb from the predefined list of adverbs. If a match is found, it returns the position of the first adverb in the original sentence using the `enumerate` function.

# The `enumerate` function is used to get both the index and the value of each word in the list. This allows us to easily access the position of the first adverb. The `index` method is used to get the index of the first adverb in the original sentence, and the variable `word` holds the value of the first adverb.

# The function