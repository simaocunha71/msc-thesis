
def select_words(s, n):
    vowels = 'aeiou'
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonants += 1
        if consonants == n:
            result.append(word)
    return result

print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))


# Output:
# ['little']
# ['Mary', 'lamb']
# []
# ['world']
# ['Uncle']

Explanation:

This function splits the input string into words and checks each word for the number of consonants. If a word has the same number of consonants as the input number, the word is added to the result list.
The result list is then returned.
"""

def select_words(s, n):
    vowels = 'aeiou'
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonants += 1
        if consonants == n:
            result.append(word)
    return result

print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))

# Output:
# ['little']
# ['Mary', 'lamb']
# []
# ['world']
# ['Uncle']
<jupyter_output>
['little']
['Mary', 'lamb']
[]
['world']
['Uncle']
<jupyter_text>
Question 