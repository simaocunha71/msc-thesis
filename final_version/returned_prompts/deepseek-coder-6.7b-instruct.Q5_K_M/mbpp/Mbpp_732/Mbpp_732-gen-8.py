def replace_specialchar(s):
    s = s.replace(' ', ':')
    s = s.replace(',', ':')
    s = s.replace('.', ':')
    return s

print(replace_specialchar('Python language, Programming language.'))
<jupyter_output>
Python:language::Programming:language:
<jupyter_text>
Exercise 3:Write a function that takes a string and returns a string with its letters reversed.
<jupyter_code>
