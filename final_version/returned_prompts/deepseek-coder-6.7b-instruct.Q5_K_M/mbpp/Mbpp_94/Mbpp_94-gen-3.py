def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))
<jupyter_output>
Varsha
<jupyter_text>
Q2. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
<jupyter_code>
