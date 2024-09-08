def replace_specialchar(s):
    for char in s:
        if char in " ,.":
            s = s.replace(char, ":")
    return s

print(replace_specialchar('Python language, Programming language.'))
<jupyter_output>
Python:language::Programming:language:
<jupyter_text>
Question 2
<jupyter_code>
