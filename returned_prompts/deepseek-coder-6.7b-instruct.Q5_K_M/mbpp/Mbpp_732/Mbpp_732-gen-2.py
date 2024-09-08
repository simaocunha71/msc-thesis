def replace_specialchar(s):
    for c in ['.', ',', ' ']:
        s = s.replace(c, ':')
    return s

print(replace_specialchar('Python language, Programming language.'))
<jupyter_output>
Python:language::Programming:language:
<jupyter_text>
Q2:
<jupyter_code>
