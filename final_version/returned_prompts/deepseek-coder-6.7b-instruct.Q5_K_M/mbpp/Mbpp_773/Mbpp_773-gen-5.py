def occurance_substring(text,sub):
    pos = text.find(sub)
    if pos != -1:
        return (sub, pos, pos+len(sub))
    else:
        return None

print(occurance_substring('python programming, python language','python'))

#Output: ('python', 0, 6)


