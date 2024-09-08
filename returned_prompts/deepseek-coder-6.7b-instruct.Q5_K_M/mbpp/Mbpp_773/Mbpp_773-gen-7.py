
def occurrence_substring(s, sub):
    pos = s.find(sub)
    if pos != -1:
        return (sub, pos, pos + len(sub))
    else:
        return None

print(occurrence_substring('python programming, python language','python'))

#Output: ('python', 0, 6)

#Here, 'python' is the substring that we are searching for in the string 'python programming, python language'. 
#The first occurrence of 'python' starts at index 0 and ends at index 6.
<jupyter_output>
('python', 0, 6)
<jupyter_text>
