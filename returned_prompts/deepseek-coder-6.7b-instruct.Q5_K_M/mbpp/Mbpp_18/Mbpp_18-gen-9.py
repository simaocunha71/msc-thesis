def remove_dirty_chars(s1, s2):
    for i in s2:
        if i in s1:
            s1 = s1.replace(i, '')
    return s1

print(remove_dirty_chars("probasscurve", "pros"))
<jupyter_output>
bacuve
<jupyter_text>
Question 2
<jupyter_code>
