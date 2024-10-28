def select_words(s, n):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    words = s.split()
    result = []
    for word in words:
        consonants = [char for char in word if char.isalpha() and char not in vowels]
        if len(consonants) == n:
            result.append(word)
    return result

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]