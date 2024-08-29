def string_to_tuple(s):
    return tuple(s)

print(string_to_tuple("python 3.0"))

# OUTPUT:
# ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')

# The space character is included in the tuple as well. If you want to exclude space, you can modify the function like this:

def string_to_tuple(s):
    return tuple(c for c in s if c != ' ')

print(string_to_tuple("python 3.0"))

# OUTPUT:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<jupyter_output>
('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<jupyter_text>
1.4: Write a Python function to convert a given list of tuples into a dictionary.
<jupyter_code>
