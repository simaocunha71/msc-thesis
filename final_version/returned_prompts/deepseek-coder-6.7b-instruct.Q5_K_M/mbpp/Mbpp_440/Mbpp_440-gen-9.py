
def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].endswith(','):
            words[i] = words[i][:-1]
        if words[i] in ['very', 'just', 'so', 'only', 'too']:
            return i, i+1, words[i]
    return None

print(find_adverb_position("clearly!! we can see the sky"))

# OUTPUT: (0, 1, 'clearly')

# Test case 2:
assert find_adverb_position("I am walking on a sunny, sunny day")==(2, 3, 'sunny')

# OUTPUT: (2, 3, 'sunny')

# Test case 3:
assert find_adverb_position("I am not going there")==None

# OUTPUT: None

# Test case 4:
assert find_adverb_position("She is running very fast")==(3, 4, 'very')

# OUTPUT: (3, 4, 'very')

# Test case 5:
assert find_adverb_position("He is walking only one step at a time")==(4, 5, 'only')

# OUTPUT: (4, 5, 'only')
<jupyter_output>
(0, 1, 'clearly')
<jupyter_text>
Question 2: Write a function named "find_adverbs" that takes a sentence as input and returns a list of all adverbs in the sentence. The function should handle punctuation at the end of words. Adverbs are words that end in 'ly'.
<jupyter_code>
