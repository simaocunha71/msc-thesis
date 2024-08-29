def split(word):
    return [char for char in word]

print(split('python'))

# Output: ['p', 'y', 't', 'h', 'o', 'n']

#Solution 2:
def split(word):
    return list(word)

print(split('python'))

# Output: ['p', 'y', 't', 'h', 'o', 'n']

#Solution 3:
def split(word):
    return [letter for letter in word]

print(split('python'))

# Output: ['p', 'y', 't', 'h', 'o', 'n']
<jupyter_output>
['p', 'y', 't', 'h', 'o', 'n']
['p', 'y', 't', 'h', 'o', 'n']
['p', 'y', 't', 'h', 'o', 'n']
<jupyter_text>
