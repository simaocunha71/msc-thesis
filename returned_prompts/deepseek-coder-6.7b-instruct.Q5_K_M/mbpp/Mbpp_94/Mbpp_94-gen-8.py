def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))
<jupyter_output>
Varsha
<jupyter_text>
4. Write a Python program to find the sum of all items in a dictionary.
<jupyter_code>
