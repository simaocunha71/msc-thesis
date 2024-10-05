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
    s = S.split(".")
    s = [i.split("?") for i in s]
    s = [i.split("!") for i in s]
    s = [i for sublist in s for i in sublist]
    return sum([1 for i in s if i.strip().startswith("I")])

print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I am bored! I don't know what to do. I am so bored. I am so bored!"))
print(is_bored("The sky is blue. The sun is shining. I love this weather. I am not bored. I am happy."))