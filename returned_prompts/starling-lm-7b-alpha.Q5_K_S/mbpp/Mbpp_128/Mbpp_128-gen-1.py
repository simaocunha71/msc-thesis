"""
def long_words(n,string):
    words = string.split()
    long_words = []
    for i in words:
        if(len(i)>n):
            long_words.append(i)
    return long_words
"""

def long_words(n,string):
    return [i for i in string.split() if len(i)>n]

print(long_words(3,"python is a programming language"))
print(long_words(3,"This is a long sentence and it has many words"))
print(long_words(3,"This is a short sentence and it has few words"))

# assert long_words(3,"python is a programming language")==['python','programming','language']
# assert long_words(3,"This is a long sentence and it has many words")==['sentence','long','it','has','many','words']
# assert long_words(3,"This is a short sentence and it has few words")==[]

```
