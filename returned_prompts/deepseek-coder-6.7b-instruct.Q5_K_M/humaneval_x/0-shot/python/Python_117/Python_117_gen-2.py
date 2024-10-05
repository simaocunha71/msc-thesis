
def select_words(s, n):
    vowels = "aeiou"
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
<jupyter_output>
['little']
['Mary', 'lamb']
[]
['world']
['Uncle']
<jupyter_text>
Question 3:
<jupyter_code>
