
def select_words(s, n):
    # split input string into words
    words = s.split()
    # initialize an empty list to store results
    results = []
    # iterate over each word
    for word in words:
        # check if word contains exactly n consonants
        if len([c for c in word if c.islower() and not c.isalpha()]) == n:
            # if so, add word to results
            results.append(word)
    # return results
    return results