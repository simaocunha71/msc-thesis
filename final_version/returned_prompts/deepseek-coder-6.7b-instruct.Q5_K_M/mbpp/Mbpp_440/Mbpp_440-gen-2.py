def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if words[i].lower() in ['well', 'not', 'just', 'so', 'only', 'too']:
            return i, i+1, words[i]
    return None

print(find_adverb_position("clearly!! we can see the sky"))
<jupyter_output>
(0, 1, 'clearly')
<jupyter_text>
Q3. Write a function named "find_word_position" that takes two parameters, a sentence and a word. The function should return the first position of the word in the sentence. If the word is not in the sentence, return -1.
<jupyter_code>
# Your code goes here
def find_word_position(sentence, word):
    position = sentence.find(word)
    if position != -1:
        return position
    else:
        return -1

print(find_word_position("Hello, World!!", "World"))
<jupyter_output>
8
<jupyter_text>
Q4. Write a function named "count_special_characters" that takes a string as an input and returns the count of special characters in it. Special characters are any character that is not alphanumeric (a-z, A-Z, 0-9).
<jupyter_code>
# Your code goes here
def count_special_characters(string):
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    count = 0
    for char in string:
        if char in special_characters:
            count += 1
    return count

print(count_special_characters("Hello, World!! How's it going?"))
<jupyter_output>
7
<jupyter_text>
Q5. Write a function named "reverse_string" that takes a string as an input and returns the reversed string.
<jupyter_code>
# Your