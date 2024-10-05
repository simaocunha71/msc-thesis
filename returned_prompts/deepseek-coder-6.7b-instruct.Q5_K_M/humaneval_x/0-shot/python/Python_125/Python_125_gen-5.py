
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for ch in txt:
            if ch.islower() and (ord(ch) - ord('a')) % 2 != 0:
                count += 1
        return count

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
print(split_words("a b c d e f"))
print(split_words("a,b,c,d,e,f"))
<jupyter_output>
['Hello', 'world!!']
['Hello', 'world!!']
3
3
3
<jupyter_text>
Exercise 2:
<jupyter_code>
