def select_words(s, n):
    def is_consonant(c):
        return c.lower() in "bcdfghjklmnpqrstvwxyz"

    words = s.split()
    result = [word for word in words if sum(is_consonant(c) for c in word) == n]
    return result

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]