def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    return len([i for i in S.split('.') if i.strip() and i.strip().startswith('I')]) + len([i for i in S.split('?') if i.strip() and i.strip().startswith('I')]) + len([i for i in S.split('!') if i.strip() and i.strip().startswith('I')])

print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I am bored. I am bored. I am bored."))
print(is_bored("The sky is blue. I am not bored. The sun is shining."))
print(is_bored("I am bored. The sky is blue. I am not bored. The sun is shining."))