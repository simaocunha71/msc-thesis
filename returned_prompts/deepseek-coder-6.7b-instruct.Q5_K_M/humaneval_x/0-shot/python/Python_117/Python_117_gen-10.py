
def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split(" ")
    result = []

    for word in words:
        count = 0
        for letter in word:
            if letter.lower() not in vowels:
                count += 1
        if count == n:
            result.append(word)

    return result

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]

# The function works by splitting the input string into a list of words. Then it iterates over each word, counting the number of consonants. If the number of consonants equals to the given number n, it appends the word to the result list. Finally, it returns the result list.

# Note: The function is case insensitive. It treats uppercase and lowercase letters as the same.
<jupyter_output>
['little']
['Mary', 'lamb']
[]
['world']
['Uncle']
<jupyter_text>
