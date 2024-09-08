
def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].lower() in ['very', 'just', 'so', 'much', 'too', 'as', 'as much', 'as often', 'as often as', 'often', 'often as', 'as much as', 'very much', 'very often', 'very often as']:
            return i, i+1, words[i]
    return -1, -1, ""

print(find_adverb_position("clearly!! we can see the sky"))

# This function first splits the sentence into words. Then it checks each word if it's an adverb. If it is, it returns the position of that adverb in the sentence. If there's no adverb, it returns -1, -1, "".

# Please note that the list of adverbs is not exhaustive and you should add the ones you need.

# Also, this function doesn't handle punctuation very well. It assumes that the adverbs are separated by spaces. In a real application, you would probably want to use a more sophisticated method to handle punctuation and other edge cases.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
