def occurance_substring(s, sub):
    pos = s.find(sub)
    if pos != -1:
        return (sub, pos, pos+len(sub))
    return None

print(occurance_substring('python programming, python language','python'))

#Output: ('python', 0, 6)

#Task 2
