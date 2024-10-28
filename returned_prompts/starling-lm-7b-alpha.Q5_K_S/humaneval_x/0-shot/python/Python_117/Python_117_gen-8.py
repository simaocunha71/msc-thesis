
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        count = 0
        for letter in word:
            if letter not in "aeiou":
                count += 1
            if count == n:
                result.append(word)
                break
    return result

# Test cases
print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]


def select_words(s, n):
    # Split the string into words
    words = s.split()
    result = []
    # Iterate through the words
    for word in words:
        # Initialize the consonant counter
        count = 0
        # Iterate through the letters of the word
        for letter in word:
            # If the letter is not a vowel, increment the counter
            if letter not in "aeiou":
                count += 1
            # If the counter matches the desired number of consonants, append the word to the result and break
            if count == n:
                result.append(word)
                break
    # Return the result
    return result

# Test cases
print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]


def select_words(s, n):
    # Split the string into words
    words = s.split()
    result = []