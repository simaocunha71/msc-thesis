def select_words(s, n):
    words = s.split()
    consonant_counts = [sum(1 for c in word if c.lower() not in 'aeiou') for word in words]
    return [word for word, count in zip(words, consonant_counts) if count == n]

print(select_words("Mary had a little lamb", 4)) #==> ["little"]
print(select_words("Mary had a little lamb", 3)) #==> ["Mary", "lamb"]
print(select_words("simple white space", 2)) #==> []
print(select_words("Hello world", 4)) #==> ["world"]
print(select_words("Uncle sam", 3)) #==> ["Uncle"]