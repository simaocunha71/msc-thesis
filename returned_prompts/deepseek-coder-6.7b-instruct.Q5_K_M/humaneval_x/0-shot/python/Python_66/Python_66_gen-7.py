
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

print(digitSum("abAB"))
print(digitSep("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))
print(digitSum(""))
<jupyter_output>
131
67
69
131
153
0
<jupyter_text>
Exercise 17:
<jupyter_code>
