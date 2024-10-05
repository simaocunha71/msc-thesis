
def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    words = txt.split(',')
    if len(words) > 1:
        return words
    return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1)

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words("abc,def"))
print(split_words("abcdefg"))
print(split_words("abc,defg"))
print(split_words("abcdefg,hi"))
<jupyter_output>
['Hello', 'world!]
['Hello', 'world!]
3
3
4
5
6
<jupyter_text>
Problem 2:
<jupyter_code>
