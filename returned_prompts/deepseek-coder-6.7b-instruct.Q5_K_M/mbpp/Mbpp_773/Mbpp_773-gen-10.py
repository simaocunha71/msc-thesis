
def occurance_substring(s, sub):
    start = s.find(sub)
    if start == -1:
        return None
    return (sub, start, start+len(sub)-1)


