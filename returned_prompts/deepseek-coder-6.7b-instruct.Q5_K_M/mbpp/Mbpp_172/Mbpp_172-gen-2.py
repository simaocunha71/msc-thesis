def count_occurance(s):
    return s.count('std')

print(count_occurance("letstdlenstdporstd"))

# Output: 3

#Alternative Solution
def count_occurance(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'std':
            count += 1
    return count

print(count_occurance("letstdlenstdporstd"))

# Output: 3
<jupyter_output>
3
3
<jupyter_text>
Question 2:
<jupyter_code>
