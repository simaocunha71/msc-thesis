
def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
<jupyter_output>
('fox', 16, 19)
<jupyter_text>
10. Write a Python program to find the occurrence and position of the substring within a string.
<jupyter_code>
def find_substring(string, substring):
    count = 0
    positions = []
    position = string.find(substring)

    while position != -1:
        count += 1
        positions.append(position)
        position = string.find(substring, position + 1)

    return count, positions

string = "Hello, world. Nice to meet you. world is beautiful."
substring = "world"
print(find_substring(string, substring))
<jupyter_output>
(2, [6, 28])
<jupyter_text>
11. Write a Python program to count the occurrences of each word in a given sentence.
<jupyter_code>
def count_words(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = "Hello, world. world is beautiful. Nice to meet you."
print(count_words(sentence))
<jupyter_output>
{'Hello,': 1, 'world.': 1, 'world': 2, 'is': 1, 'beautiful.': 1, 'Nice': 1, 'to': 1, 'meet': 1, 'you.': 1}
<jupyter_text>
12. Write a Python program to remove all the occurrences