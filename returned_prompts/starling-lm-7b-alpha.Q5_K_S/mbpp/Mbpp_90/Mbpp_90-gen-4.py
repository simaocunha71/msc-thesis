"""
def len_log(words):
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    return length

#test
assert len_log(["python","PHP","bigdata"]) == 7
"""

