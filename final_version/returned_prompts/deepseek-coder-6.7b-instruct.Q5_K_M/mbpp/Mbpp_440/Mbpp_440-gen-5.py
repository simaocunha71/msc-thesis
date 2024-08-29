
def find_adverb_position(sentence):
    adverbs = ["clearly", "easily", "often", "always", "never", "still", "just", "again", "further", "even", "night"]
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in adverbs:
            return i, i+1, words[i]
    return None

print(find_adverb_position("clearly!! we can see the sky"))
<jupyter_output>
(0, 1, 'clearly')
<jupyter_text>
Exercise 3:
<jupyter_code>
