
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))

# Output: 
# 131
# 67
# 69
# 131
# 153
<jupyter_output>
131
67
69
131
153
<jupyter_text>
Question 2
<jupyter_code>
