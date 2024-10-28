def select_words(s, n):
    def count_consonants(word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(1 for c in word if c.lower() not in vowels and c.isalpha())
    
    words = s.split()
    return [word for word in words if count_consonants(word) == n]

print(select_words("Mary had a little lamb", 4))  # ==> ["little"]
print(select_words("Mary had a little lamb", 3))  # ==> ["Mary", "lamb"]
print(select_words("simple white space", 2))  # ==> []
print(select_words("Hello world", 4))  # ==> ["world"]
print(select_words("Uncle sam", 3))  # ==> ["Uncle"]