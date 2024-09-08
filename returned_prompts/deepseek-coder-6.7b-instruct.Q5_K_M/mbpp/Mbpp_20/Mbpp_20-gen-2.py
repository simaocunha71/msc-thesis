
def is_woodall(n):
    s = str(n)
    l = len(s)
    for i in range(1, l):
        if int(s[:i]) * int(s[i:]) != n:
            return False
    return True

print(is_woodall(383))
<jupyter_output>
True
<jupyter_text>
Exercise 2:
<jupyter_code>
