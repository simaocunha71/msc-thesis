"""
Here is a solution to the problem using Python programming language.

```python
import nltk
from nltk.tokenize import word_tokenize

def find_adverb_position(sentence):
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    for i in range(len(pos_tags)):
        if pos_tags[i][1] == 'RB' or pos_tags[i][1] == 'RBR' or pos_tags[i][1] == 'RBS':
            return (i, i+1, pos_tags[i][0])

print(find_adverb_position("clearly!! we can see the sky"))
```

In this solution, we first tokenize the sentence into words and apply Part of Speech tagging using nltk.pos_tag. Then, we check each word's Part of Speech tag to see if it is an adverb. If we find an adverb, we return its position and value.

Please note that this solution assumes that the sentence does not contain punctuation marks. If you need to deal with punctuation, you might need to clean the sentence first.
"""

