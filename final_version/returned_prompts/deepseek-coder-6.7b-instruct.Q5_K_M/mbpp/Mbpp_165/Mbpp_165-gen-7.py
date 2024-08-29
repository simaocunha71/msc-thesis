def count_char_position(s):
    return sum(1 for c, a in zip(s, map(ord, "abcdefghijklmnopqrstuvwxyz")) if c.lower() == chr(a + 97))

print(count_char_position("xbcefg"))
<jupyter_output>
2
<jupyter_text>
Exercise 3
<jupyter_code>
