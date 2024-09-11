"""
def len_log(list_words):
    # Get the length of the longest word
    length = 0
    for word in list_words:
        if len(word) > length:
            length = len(word)
    return length

# Test
print(len_log(["python","PHP","bigdata"])) # Output: 7
"""

