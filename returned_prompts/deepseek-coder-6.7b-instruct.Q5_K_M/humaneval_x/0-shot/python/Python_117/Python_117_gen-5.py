
def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split(" ")
    consonants = [word for word in words if sum(ch not in vowels for ch in word.lower()) == n]
    return consonants

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]

# Alternative solution:

def select_words(s, n):
    return [word for word in s.split() if sum(ch not in 'aeiou' for ch in word.lower()) == n]

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]

# Alternative solution:

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        count = 0
        for ch in word:
            if ch.lower() not in 'aeiou':
                count += 1
        if count == n:
            result.append(word)
    return result

print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 