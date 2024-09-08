def occurance_substring(s, sub_s):
    pos = s.find(sub_s)
    if pos != -1:
        return (sub_s, pos, pos+len(sub_s))