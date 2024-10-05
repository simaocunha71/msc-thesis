
def find_max(words):
    def count_chars(word):
        return len(set(word))
    return max(words, key=count_chars)

def find_max(words):
    def count_chars(word):
        return len(set(word))
    return max(words, key=count_chars)

print(find_max(["name", "of", "string"])) # "string"
print(find_max(["name", "enam", "game"])) # "enam"
print(find_max(["aaaaaaa", "bb", "cc"])) # "aaaaaaa"




# Other solutions
def find_max(words):
    return max(words, key=lambda x: (len(set(x)), x))

from functools import *
def find_max(words):
    return max(words, key=cmp_to_key(lambda a, b: cmp(len(set(a)), len(set(b))) if len(set(a)) != len(set(b)) else cmp(a,b)))

def find_max(words):
    return max(words, key=lambda x: (len(set(x)), x))

from functools import *
def find_max(words):
    return max(words, key=cmp_to_key(lambda a, b: cmp(len(set(a)), len(set(b))) if len(set(a)) != len(set(b)) else cmp(a,b)))





















































































































































