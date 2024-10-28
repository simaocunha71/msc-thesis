    boredom = 0
    current_sentence = ""
    for c in S:
        if c == '.' or c == '!' or c == '?':
            if current_sentence.startswith('I'):
                boredom += 1
            current_sentence = ""
        else:
            current_sentence += c
    return boredom


# Other solutions
from itertools import groupby
from operator import itemgetter

def is_bored(S):
    for k, g in groupby(S, itemgetter(0)):
        if k == 'I' and any(c in '.?! ' for c in g):
            return True
    return False


def is_bored(S):
    sentence = ""
    for c in S:
        if c in ['.', '?', '!']:
            if sentence.startswith('I'):
                return True
            sentence = ""
        else:
            sentence += c
    return False


# Alternative solution using regex
import re

def is_bored(S):
    return len(re.findall(r'^I.*[.?!]', S)) != 0


if __name__ == '__main__':
    print(is_bored("Hello world"))  # 0
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # 1
    print(is_bored("I love Python"))  # 1
    print(is_bored("I love Python!"))  # 1
    print(is_bored("I love Python! I also love Ruby."))  # 2


















































































































