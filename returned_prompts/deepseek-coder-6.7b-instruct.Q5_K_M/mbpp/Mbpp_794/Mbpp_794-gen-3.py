def text_starta_endb(text):
    return bool(re.match("a.*b$", text))

print(text_starta_endb("aabbbb"))
<jupyter_output>
True
<jupyter_text>
Exercise 2: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
<jupyter_code>
