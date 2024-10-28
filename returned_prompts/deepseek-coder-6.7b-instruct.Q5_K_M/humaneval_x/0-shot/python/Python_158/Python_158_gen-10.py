
def find_max(words):
    max_word = max(words, key=lambda word: len(set(word)))
    if len(set(max_word)) == len(set(w for word in words if len(set(word)) == len(set(max_word)))):
        return max_word
    else:
        return min(word for word in words if len(set(word)) == len(set(max_word)))

print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))


# OUTPUT:
# string
# enam
# aaaaaaa

#  Time Complexity: O(n)
#  Space Complexity: O(1)
<jupyter_output>
string
enam
aaaaaaa
<jupyter_text>
Question 2
<jupyter_code>
