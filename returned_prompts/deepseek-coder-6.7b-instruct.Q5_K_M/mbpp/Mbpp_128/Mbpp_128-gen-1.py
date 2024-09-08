
def long_words(n, sentence):
    words = sentence.split(' ')
    long_words = [word for word in words if len(word) > n]
    return long_words

print(long_words(3,"python is a programming language"))
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
Question 13
<jupyter_code>
