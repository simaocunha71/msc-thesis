def select_words(s, n):
    vowels = "aeiou"
    words = s.split()
    res = []
    for word in words:
        if len([c for c in word.lower() if c not in vowels]) == n:
            res.append(word)
    return res

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]