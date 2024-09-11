def remove_length(string, k):
    """
    Remove all the words with k length in the given string
    """
    words = string.split()
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    return " ".join(new_words)

# Test
assert remove_length('The person is most value tet', 3) == 'person is most value'

def remove_length(string, k):
    """
    Remove all the words with k length in the given string
    """
    words = string.split()
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    return " ".join(new_words)

# Test
assert remove_length('The person is most value tet', 3) == 'person is most value'

# More Test
assert remove_length("It's a long day today", 4) == "It's a day today"
assert remove_length("I have a very short day", 3) == "I have a day"
assert remove_length("It's a long day today", 2) == "It's day today"

# Extra Test
assert remove_length("I have a very short day", 4) == "I have a day"
assert remove_length("It's a long day today", 1) == "It's day today"

# Extra Test
assert remove_length("It's a long day today", 5) == "It's day today"
assert remove_length("I have a very short day", 6) == "I have a day"

# Extra Test
assert remove_length("It's a long day today", 0) == "It's day today"
assert remove_length("I have a very short day", 0) == "I have a day"

# Extra Test
assert remove_length("It's a long day today", 7) == "It's day today"
assert remove_length("I have a very short day", 7) == "I have a day"
