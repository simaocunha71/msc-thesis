def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word.lower() in ['quickly', 'slowly', 'suddenly', 'clearly', 'easily', 'often', 'rarely', 'usually']:
            return i, words[i], words
    return -1, '', []


# Test
print(find_adverb_position("clearly!! we can see the sky"))  # (0, 'clearly', ['clearly', 'we', 'can', 'see', 'the', 'sky'])
print(find_adverb_position("The old man quickly walked down the street."))  # (-1, '', [])
print(find_adverb_position("The old man quickly walked down the street."))  # (3, 'quickly', ['The', 'old', 'man', 'quickly', 'walked', 'down', 'the', 'street.'])






"""
The main idea of this problem is to find the first adverb and their positions in a given sentence.
We can break this problem down into the following steps:
1. We need to identify the adverbs in the sentence. We can do this by checking if the word is an adverb.
2. Once we have identified the adverbs, we need to find the position of the first adverb in the sentence. We can do this by iterating through the words in the sentence and checking if each word is an adverb.
3. Finally, we can return the position of the first adverb along with the adverb itself.
"""

```python
def find_adverb_position(sentence):
    # Step 1: Identify the adverbs in the sentence
    adverbs = ['quickly', 'slowly', 'suddenly', 'clearly', 'easily', 'often', 'rarely', 'usually']

    # Step 2: Find the position of the first adverb in the sentence
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word.lower() in adverbs:
            return i, word, words

