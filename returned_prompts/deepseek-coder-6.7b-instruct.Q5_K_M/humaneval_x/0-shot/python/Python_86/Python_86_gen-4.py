
def anti_shuffle(s):
    words = s.split(' ')
    res = []
    for word in words:
        new_word = ''.join(sorted(word))
        res.append(new_word)
    return ' '.join(res)

# Test cases
print(anti_shuffle('Hi'))  # 'Hi'
print(anti_shuffle('hello'))  # 'ehllo'
print(anti_shuffle('Hello World!!!'))  # 'Hello !!!Wdlor'

# This solution works by splitting the input string into words,
# sorting the characters in each word and then joining them back together.
# The order of the words is preserved as the sorted function maintains the original order of equal elements.
# If the original word has uppercase letters, they are ordered before lowercase letters due to ASCII values.

# Note: This solution assumes that words are separated by space characters and that punctuation is treated as part of the word.
# If this is not the case, the solution would need to be adjusted accordingly.
# For example, 'Hello,World!!!' would be sorted as ',Hello!!!Wdlor' if words are separated by commas.
<jupyter_output>
Hi
ehllo
Hello  !!!Wdlor
<jupyter_text>
3. Write a Python function to find the sum of the squares of the digits of a number.
<jupyter_code>
