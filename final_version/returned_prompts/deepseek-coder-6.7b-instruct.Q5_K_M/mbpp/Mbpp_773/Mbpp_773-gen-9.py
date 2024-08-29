def occurance_substring(s, sub_s):
    pos = s.find(sub_s)
    if pos != -1:
        return (sub_s, pos, pos+len(sub_s))

print(occurance_substring('python programming, python language','python'))

# Output: ('python', 0, 6)

"""
In the above function, we use the find() method which returns the lowest index of the substring (if found). If not found, it returns -1. 
Then, if substring is found, we return the substring, its starting position and its end position. We calculate end position by adding the length of the substring to the starting position.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
