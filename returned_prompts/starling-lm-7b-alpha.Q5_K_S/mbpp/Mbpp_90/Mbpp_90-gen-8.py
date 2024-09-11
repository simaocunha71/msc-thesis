"""
def len_log(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

# Test
assert len_log(["python","PHP","bigdata"]) == 7
"""

