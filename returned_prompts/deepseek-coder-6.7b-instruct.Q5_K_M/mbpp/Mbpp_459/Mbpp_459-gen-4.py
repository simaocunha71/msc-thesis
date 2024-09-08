def remove_uppercase(s):
    s = list(s)
    i = 0
    while i < len(s):
        if s[i].isupper():
            s.pop(i)
        else:
            i += 1
    return "".join(s)

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
<jupyter_output>
cstyoravoitshos
<jupyter_text>
Question 3
<jupyter_code>
