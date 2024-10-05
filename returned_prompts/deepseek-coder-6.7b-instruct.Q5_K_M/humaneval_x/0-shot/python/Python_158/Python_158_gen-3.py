
def find_max(words):
    max_unique = 0
    max_word = ''
    for word in words:
        unique = len(set(word))
        if unique > max_unique:
            max_unique = unique
            max_word = word
        elif unique == max_unique:
            if word < max_word:
                max_word = word
    return max_word

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))

# Output:
# string
# enam
# aaaaaaa
<jupyter_output>
string
enam
aaaaaaa
<jupyter_text>
**Problem 2:**
<jupyter_code>
