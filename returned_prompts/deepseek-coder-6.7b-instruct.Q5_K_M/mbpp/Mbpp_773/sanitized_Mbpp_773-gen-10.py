def occurance_substring(str1,str2):
    pos = str1.find(str2)
    if pos != -1:
        return (str2, pos, pos+len(str2))
    else:
        return None