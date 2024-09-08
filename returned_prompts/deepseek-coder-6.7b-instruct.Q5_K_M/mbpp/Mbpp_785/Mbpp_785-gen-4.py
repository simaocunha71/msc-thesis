def tuple_str_int(s):
    s = s.strip('()')
    s = map(int, s.split(','))
    return tuple(s)

# test
print(tuple_str_int("(7, 8, 9)"))

# Output:
# (7, 8, 9)
<jupyter_output>
(7, 8, 9)
<jupyter_text>
Question 6
<jupyter_code>
